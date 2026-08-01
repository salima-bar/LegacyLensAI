import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Plus, Filter, Terminal } from "lucide-react";
import { TopBar } from "@/components/TopBar";
import { ScoreRing } from "@/components/ScoreRing";
import { StatusBadge } from "@/components/StatusBadge";
import { PROJECTS } from "@/data/mockData";
import type { Project, ProjectStatus } from "@/types";

const TOKEN_STORAGE_KEY = "legacylens_access_token";

type FilterKey = "all" | ProjectStatus;

const FILTERS: { key: FilterKey; label: string }[] = [
  { key: "all", label: "All" },
  { key: "risk", label: "At risk" },
  { key: "review", label: "Needs review" },
  { key: "healthy", label: "Healthy" },
];

interface BackendProjectResponse {
  id: string;
  name: string;
  description?: string | null;
  original_file_name: string;
  status: string;
  upload_date: string;
  last_analysis_date?: string | null;
  current_analysis_id?: string | null;
  user_id: string;
}

function mapBackendStatus(status: string): ProjectStatus {
  switch (status) {
    case "Analyzing":
      return "scanning";
    case "Completed":
      return "healthy";
    case "Failed":
      return "risk";
    default:
      return "review";
  }
}

function mapBackendProject(project: BackendProjectResponse): Project {
  const stack = [project.original_file_name.split(".").pop() || "Archive"];
  const score = project.status === "Completed" ? 72 : project.status === "Analyzing" ? 58 : project.status === "Failed" ? 29 : 51;

  return {
    id: project.id,
    name: project.name,
    stack,
    score,
    status: mapBackendStatus(project.status),
    files: 0,
    lastScan: project.last_analysis_date ? new Date(project.last_analysis_date).toLocaleDateString() : "Not scanned",
    risks: project.status === "Failed" ? 22 : project.status === "Completed" ? 6 : 11,
  };
}

export function Projects() {
  const [filter, setFilter] = useState<FilterKey>("all");
  const [projects, setProjects] = useState<Project[]>(PROJECTS);
  const navigate = useNavigate();

  useEffect(() => {
    const token = window.localStorage.getItem(TOKEN_STORAGE_KEY);

    if (!token) {
      return;
    }

    fetch("/projects", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(async (response) => {
        if (!response.ok) {
          return;
        }

        const payload = (await response.json()) as BackendProjectResponse[];
        const mapped = payload.map(mapBackendProject);

        if (mapped.length > 0) {
          setProjects(mapped);
        }
      })
      .catch(() => {
        // Preserve the existing page layout and let the mock fallback remain visible while the backend payload is unavailable.
      });
  }, []);

  const filtered = filter === "all" ? projects : projects.filter((p) => p.status === filter);

  return (
    <>
      <TopBar title="Projects" subtitle="All connected codebases" />
      <div className="ll-scrollable" style={{ flex: 1, overflowY: "auto", padding: "32px 36px 60px" }}>
        <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", marginBottom: 22 }}>
          <div>
            <div className="ll-display" style={{ fontSize: 22, fontWeight: 600 }}>Projects</div>
            <div style={{ fontSize: 13, color: "var(--text-2)", marginTop: 4 }}>{projects.length} legacy codebases connected</div>
          </div>
          <button className="ll-btn ll-btn-primary" style={{ padding: "9px 16px", borderRadius: 8, fontSize: 13 }}>
            <Plus size={14} /> Upload project
          </button>
        </div>

        <div style={{ display: "flex", gap: 6, marginBottom: 16 }}>
          {FILTERS.map((f) => (
            <button
              key={f.key}
              onClick={() => setFilter(f.key)}
              className="ll-btn"
              style={{
                padding: "6px 12px",
                borderRadius: 7,
                fontSize: 12.5,
                background: filter === f.key ? "var(--surface-2)" : "transparent",
                color: filter === f.key ? "var(--text)" : "var(--text-3)",
                border: `1px solid ${filter === f.key ? "var(--border)" : "transparent"}`,
              }}
            >
              {f.label}
            </button>
          ))}
          <div style={{ flex: 1 }} />
          <button className="ll-btn ll-btn-ghost" style={{ padding: "6px 12px", borderRadius: 7, fontSize: 12.5 }}>
            <Filter size={13} /> Sort
          </button>
        </div>

        <div className="ll-card" style={{ overflow: "hidden" }}>
          <div className="ll-mono" style={{ display: "grid", gridTemplateColumns: "2.2fr 1.6fr 0.8fr 0.9fr 0.9fr 0.6fr", padding: "10px 18px", fontSize: 10.5, color: "var(--text-3)", borderBottom: "1px solid var(--border)" }}>
            <span>PROJECT</span><span>STACK</span><span>SCORE</span><span>STATUS</span><span>LAST SCAN</span><span>RISKS</span>
          </div>
          {filtered.map((p) => (
            <div
              key={p.id}
              className="ll-table-row"
              style={{ display: "grid", gridTemplateColumns: "2.2fr 1.6fr 0.8fr 0.9fr 0.9fr 0.6fr", alignItems: "center", padding: "13px 18px", cursor: "pointer" }}
              onClick={() => navigate(`/app/analysis/${p.id}`)}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                <div style={{ width: 30, height: 30, borderRadius: 8, background: "var(--surface-2)", border: "1px solid var(--border)", display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0 }}>
                  <Terminal size={13} color="var(--text-2)" />
                </div>
                <span style={{ fontSize: 13, fontWeight: 500 }}>{p.name}</span>
              </div>
              <div style={{ display: "flex", gap: 5, flexWrap: "wrap" }}>{p.stack.slice(0, 2).map((t) => <span key={t} className="ll-tag">{t}</span>)}</div>
              <ScoreRing score={p.score} size={30} stroke={3} />
              <div><StatusBadge status={p.status} /></div>
              <span className="ll-mono" style={{ fontSize: 11.5, color: "var(--text-3)" }}>{p.lastScan}</span>
              <span className="ll-mono" style={{ fontSize: 12, color: p.risks > 15 ? "var(--red)" : "var(--text-2)" }}>{p.risks}</span>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
