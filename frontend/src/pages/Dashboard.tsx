import { useNavigate } from "react-router-dom";
import {
  ResponsiveContainer, LineChart, Line, YAxis, Tooltip as RTooltip,
} from "recharts";
import { Upload, ArrowRight, ChevronRight, ShieldAlert, TrendingUp, Clock, Boxes, Database } from "lucide-react";
import { TopBar } from "@/components/TopBar";
import { ScoreRing } from "@/components/ScoreRing";
import { StatusBadge } from "@/components/StatusBadge";
import { PROJECTS, TREND, RISKS } from "@/data/mockData";

const STATS = [
  { label: "Projects scanned", value: "12", icon: Boxes, delta: "+2 this month" },
  { label: "Open risks", value: "34", icon: ShieldAlert, delta: "6 critical" },
  { label: "Avg modernization score", value: "62", icon: TrendingUp, delta: "+5 vs last month" },
  { label: "Engineering hours saved", value: "480", icon: Clock, delta: "estimated" },
];

export function Dashboard() {
  const navigate = useNavigate();
  const openProject = (id: string) => navigate(`/app/analysis/${id}`);

  return (
    <>
      <TopBar title="Dashboard" subtitle="Overview of everything LegacyLensAI has found" />
      <div className="ll-scrollable" style={{ flex: 1, overflowY: "auto", padding: "32px 36px 60px" }}>
        <div className="ll-fade-up" style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", marginBottom: 28 }}>
          <div>
            <div className="ll-display" style={{ fontSize: 24, fontWeight: 600 }}>Good afternoon, Sara</div>
            <div style={{ fontSize: 13, color: "var(--text-2)", marginTop: 4 }}>Meridian Systems workspace · Friday, August 1</div>
          </div>
          <button className="ll-btn ll-btn-primary" style={{ padding: "9px 16px", borderRadius: 8, fontSize: 13 }} onClick={() => navigate("/app/projects")}>
            <Upload size={14} /> Analyze a project
          </button>
        </div>

        {/* Stat strip */}
        <div className="ll-fade-up" style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 14, marginBottom: 24 }}>
          {STATS.map((s) => (
            <div key={s.label} className="ll-card" style={{ padding: "16px 18px" }}>
              <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 14 }}>
                <span style={{ fontSize: 12, color: "var(--text-2)" }}>{s.label}</span>
                <s.icon size={14} color="var(--text-3)" strokeWidth={1.8} />
              </div>
              <div className="ll-display" style={{ fontSize: 26, fontWeight: 600 }}>{s.value}</div>
              <div className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)", marginTop: 4 }}>{s.delta}</div>
            </div>
          ))}
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1.55fr 1fr", gap: 14, marginBottom: 14, alignItems: "stretch" }}>
          {/* Continue analysis */}
          <div className="ll-card ll-fade-up" style={{ padding: 20, display: "flex", flexDirection: "column", gap: 16 }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
              <div style={{ fontSize: 13, fontWeight: 600, color: "var(--text)" }}>Continue where you left off</div>
              <StatusBadge status="scanning" />
            </div>
            <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
              <div style={{ width: 44, height: 44, borderRadius: 10, background: "var(--surface-2)", border: "1px solid var(--border)", display: "flex", alignItems: "center", justifyContent: "center" }}>
                <Database size={18} color="var(--accent)" strokeWidth={1.8} />
              </div>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 14, fontWeight: 600 }}>Atlas Claims Engine</div>
                <div className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)", marginTop: 3 }}>Generating recommendations · stage 3 of 5</div>
                <div className="ll-progress-track" style={{ height: 5, marginTop: 10 }}>
                  <div className="ll-progress-fill" style={{ width: "58%" }} />
                </div>
              </div>
              <button className="ll-btn ll-btn-subtle" style={{ padding: "8px 14px", borderRadius: 7, fontSize: 12 }} onClick={() => openProject("atlas-claims-engine")}>
                Resume <ArrowRight size={13} />
              </button>
            </div>
            <div style={{ display: "flex", gap: 8, marginTop: 2 }}>
              {["Overview", "Documentation", "Architecture", "Recommendations", "Roadmap"].map((s, i) => (
                <div key={s} style={{ flex: 1, textAlign: "center" }}>
                  <div style={{ height: 3, borderRadius: 2, background: i < 3 ? "var(--accent)" : "var(--border)", marginBottom: 6 }} />
                  <div className="ll-mono" style={{ fontSize: 9.5, color: i < 3 ? "var(--text-2)" : "var(--text-3)" }}>{s}</div>
                </div>
              ))}
            </div>
          </div>

          {/* Trend chart */}
          <div className="ll-card ll-fade-up" style={{ padding: 20, display: "flex", flexDirection: "column" }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 4 }}>
              <div style={{ fontSize: 13, fontWeight: 600 }}>Modernization score trend</div>
              <span className="ll-mono" style={{ fontSize: 11, color: "var(--green)" }}>+24 pts / 6mo</span>
            </div>
            <div style={{ flex: 1, minHeight: 110, marginTop: 6 }}>
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={TREND} margin={{ top: 10, right: 4, left: 4, bottom: 0 }}>
                  <YAxis hide domain={[20, 80]} />
                  <RTooltip
                    contentStyle={{ background: "#171b21", border: "1px solid #23272e", borderRadius: 8, fontSize: 12, fontFamily: "IBM Plex Mono" }}
                    labelStyle={{ color: "#8d94a3" }}
                    itemStyle={{ color: "#e8a33d" }}
                  />
                  <Line type="monotone" dataKey="score" stroke="#e8a33d" strokeWidth={2} dot={{ r: 2.5, fill: "#e8a33d", strokeWidth: 0 }} activeDot={{ r: 4 }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1.55fr 1fr", gap: 14 }}>
          {/* Projects list */}
          <div className="ll-card ll-fade-up" style={{ padding: 4 }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "14px 16px 10px" }}>
              <div style={{ fontSize: 13, fontWeight: 600 }}>Your projects</div>
              <button className="ll-btn" style={{ background: "transparent", color: "var(--text-3)", fontSize: 12 }} onClick={() => navigate("/app/projects")}>
                View all <ChevronRight size={13} />
              </button>
            </div>
            {PROJECTS.slice(0, 4).map((p) => (
              <div key={p.id} className="ll-table-row" style={{ display: "flex", alignItems: "center", gap: 14, padding: "12px 16px", cursor: "pointer" }} onClick={() => openProject(p.id)}>
                <ScoreRing score={p.score} size={34} stroke={3.5} />
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontSize: 13, fontWeight: 500 }}>{p.name}</div>
                  <div style={{ display: "flex", gap: 6, marginTop: 5 }}>
                    {p.stack.map((t) => <span key={t} className="ll-tag">{t}</span>)}
                  </div>
                </div>
                <StatusBadge status={p.status} />
                <div className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)", width: 90, textAlign: "right" }}>{p.lastScan}</div>
              </div>
            ))}
          </div>

          {/* Risk radar */}
          <div className="ll-card ll-fade-up" style={{ padding: "14px 16px" }}>
            <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 10 }}>
              <div style={{ fontSize: 13, fontWeight: 600 }}>Risk radar</div>
              <ShieldAlert size={14} color="var(--text-3)" />
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              {RISKS.map((r) => {
                const c = r.sev === "critical" ? "var(--red)" : r.sev === "warning" ? "var(--accent)" : "var(--text-3)";
                return (
                  <div key={r.id} style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
                    <div style={{ width: 6, height: 6, borderRadius: "50%", background: c, marginTop: 5, flexShrink: 0 }} />
                    <div style={{ minWidth: 0 }}>
                      <div style={{ fontSize: 12.5, color: "var(--text)", lineHeight: 1.4 }}>{r.text}</div>
                      <div className="ll-mono" style={{ fontSize: 10.5, color: "var(--text-3)", marginTop: 2, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>{r.file}</div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
