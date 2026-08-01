import type { ReactNode } from "react";
import type { Project } from "@/types";
import { ProjectHeader } from "@/features/analysis/ProjectHeader";
import { AnalysisTabs } from "@/features/analysis/AnalysisTabs";
import { AssistantPanel } from "@/features/analysis/AssistantPanel";

interface AnalysisLayoutProps {
  project: Project;
  /** The active tab's content (rendered via <Outlet /> by the Analysis page). */
  children: ReactNode;
}

/**
 * Reusable layout for the Analysis page. Every analyzed project renders
 * through this same layout: project header, horizontal tabs, and a
 * persistent AI Assistant panel that stays mounted while tabs change.
 *
 * This component owns no tab-content logic — it only arranges the
 * header, tabs, content pane, and assistant. Tab content is passed in
 * as children so it can be swapped independently.
 */
export function AnalysisLayout({ project, children }: AnalysisLayoutProps) {
  return (
    <div style={{ flex: 1, display: "flex", minHeight: 0 }}>
      <div className="ll-scrollable" style={{ flex: 1, overflowY: "auto", padding: "26px 32px 60px", minWidth: 0 }}>
        <ProjectHeader project={project} />
        <AnalysisTabs />
        {children}
      </div>
      <AssistantPanel projectName={project.name} />
    </div>
  );
}
