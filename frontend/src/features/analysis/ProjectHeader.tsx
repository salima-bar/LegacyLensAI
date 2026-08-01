import { Link } from "react-router-dom";
import { ChevronRight } from "lucide-react";
import type { Project } from "@/types";
import { StatusBadge } from "@/components/StatusBadge";

interface ProjectHeaderProps {
  project: Project;
}

export function ProjectHeader({ project }: ProjectHeaderProps) {
  return (
    <div style={{ marginBottom: 20 }}>
      <div
        className="ll-mono"
        style={{ display: "flex", alignItems: "center", gap: 8, fontSize: 11.5, color: "var(--text-3)", marginBottom: 10 }}
      >
        <Link to="/app/projects" style={{ color: "inherit", textDecoration: "none" }}>Projects</Link>
        <ChevronRight size={12} />
        <span style={{ color: "var(--text-2)" }}>{project.name}</span>
      </div>

      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 10 }}>
        <div className="ll-display" style={{ fontSize: 21, fontWeight: 600 }}>{project.name}</div>
        <StatusBadge status={project.status} />
      </div>

      <div style={{ display: "flex", alignItems: "center", gap: 14, flexWrap: "wrap" }}>
        <div style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
          {project.stack.map((t) => (
            <span key={t} className="ll-tag">{t}</span>
          ))}
        </div>
        <span className="ll-mono" style={{ fontSize: 11.5, color: "var(--text-3)" }}>
          Last analyzed {project.lastScan}
        </span>
      </div>
    </div>
  );
}
