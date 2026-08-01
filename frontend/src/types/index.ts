export type ProjectStatus = "healthy" | "risk" | "scanning" | "review";

export interface Project {
  id: string;
  name: string;
  stack: string[];
  score: number;
  status: ProjectStatus;
  files: number;
  lastScan: string;
  risks: number;
}

export interface TrendPoint {
  name: string;
  score: number;
}

export type RiskSeverity = "critical" | "warning" | "info";

export interface RiskFinding {
  id: number;
  sev: RiskSeverity;
  text: string;
  file: string;
}

export type ChatRole = "user" | "ai";

export interface ChatMessage {
  role: ChatRole;
  text: string;
}

/** Keys for the horizontal tabs on the Analysis page. Order matters — it drives both the nav and the routes. */
export const ANALYSIS_TAB_KEYS = [
  "overview",
  "documentation",
  "architecture",
  "recommendations",
  "roadmap",
] as const;

export type AnalysisTabKey = (typeof ANALYSIS_TAB_KEYS)[number];
