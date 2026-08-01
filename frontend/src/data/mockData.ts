import type { Project, TrendPoint, RiskFinding } from "@/types";

export const PROJECTS: Project[] = [
  { id: "meridian-core-banking", name: "Meridian Core Banking", stack: ["Java 8", "Struts", "Oracle 11g"], score: 41, status: "risk", files: 8420, lastScan: "2 hours ago", risks: 19 },
  { id: "atlas-claims-engine", name: "Atlas Claims Engine", stack: [".NET Framework 4.6", "SOAP", "SQL Server"], score: 58, status: "review", files: 3110, lastScan: "1 day ago", risks: 11 },
  { id: "harbor-inventory", name: "Harbor Inventory", stack: ["PHP 5.6", "MySQL 5.5"], score: 73, status: "healthy", files: 1240, lastScan: "3 days ago", risks: 4 },
  { id: "foundry-etl-pipeline", name: "Foundry ETL Pipeline", stack: ["Python 2.7", "Airflow 1.x"], score: 29, status: "risk", files: 640, lastScan: "5 days ago", risks: 26 },
  { id: "northwind-crm", name: "Northwind CRM", stack: ["Rails 4", "Ruby 2.3", "Postgres 9"], score: 66, status: "review", files: 2890, lastScan: "1 week ago", risks: 9 },
];

export const TREND: TrendPoint[] = [
  { name: "Mar", score: 38 },
  { name: "Apr", score: 44 },
  { name: "May", score: 41 },
  { name: "Jun", score: 52 },
  { name: "Jul", score: 57 },
  { name: "Aug", score: 62 },
];

export const RISKS: RiskFinding[] = [
  { id: 1, sev: "critical", text: "Hardcoded database credentials in AuthService.java", file: "src/auth/AuthService.java:112" },
  { id: 2, sev: "critical", text: "SQL built via string concatenation — injection risk", file: "src/billing/InvoiceDAO.java:88" },
  { id: 3, sev: "warning", text: "Zero test coverage across the billing module", file: "src/billing/**" },
  { id: 4, sev: "warning", text: "javax.xml.bind removed in Java 11 — will not compile", file: "src/reports/XmlExporter.java:5" },
  { id: 5, sev: "info", text: "Struts 1 reached end-of-life in 2013", file: "pom.xml" },
];

export function getProjectById(id: string | undefined): Project | undefined {
  return PROJECTS.find((p) => p.id === id);
}
