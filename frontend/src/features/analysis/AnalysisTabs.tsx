import { NavLink } from "react-router-dom";
import { LayoutGrid, BookOpen, Layers, Sparkles, Map as MapIcon } from "lucide-react";
import type { AnalysisTabKey } from "@/types";

interface TabDef {
  key: AnalysisTabKey;
  label: string;
  icon: typeof LayoutGrid;
}

const TABS: TabDef[] = [
  { key: "overview", label: "Overview", icon: LayoutGrid },
  { key: "documentation", label: "Documentation", icon: BookOpen },
  { key: "architecture", label: "Architecture", icon: Layers },
  { key: "recommendations", label: "Recommendations", icon: Sparkles },
  { key: "roadmap", label: "Roadmap", icon: MapIcon },
];

export function AnalysisTabs() {
  return (
    <div style={{ display: "flex", gap: 22, borderBottom: "1px solid var(--border)", marginBottom: 22 }}>
      {TABS.map((tab) => (
        <NavLink
          key={tab.key}
          to={tab.key}
          className={({ isActive }) => `ll-focus-line ${isActive ? "active" : ""}`}
          style={({ isActive }) => ({
            display: "flex",
            alignItems: "center",
            gap: 7,
            paddingBottom: 11,
            cursor: "pointer",
            fontSize: 13,
            textDecoration: "none",
            color: isActive ? "var(--text)" : "var(--text-3)",
            fontWeight: isActive ? 600 : 500,
          })}
        >
          <tab.icon size={14} /> {tab.label}
        </NavLink>
      ))}
    </div>
  );
}
