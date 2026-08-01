import type { ProjectStatus } from "@/types";

interface StatusBadgeProps {
  status: ProjectStatus;
}

const STATUS_MAP: Record<ProjectStatus, { color: string; bg: string; label: string }> = {
  healthy: { color: "var(--green)", bg: "var(--green-soft)", label: "Healthy" },
  risk: { color: "var(--red)", bg: "var(--red-soft)", label: "At risk" },
  scanning: { color: "var(--accent)", bg: "var(--accent-soft)", label: "Scanning" },
  review: { color: "var(--blue)", bg: "var(--blue-soft)", label: "Needs review" },
};

export function StatusBadge({ status }: StatusBadgeProps) {
  const s = STATUS_MAP[status];
  return (
    <span
      className="ll-mono"
      style={{ display: "inline-flex", alignItems: "center", gap: 6, fontSize: 11, padding: "3px 9px", borderRadius: 999, background: s.bg, color: s.color }}
    >
      <span style={{ width: 5, height: 5, borderRadius: "50%", background: s.color }} className={status === "scanning" ? "ll-pulse" : ""} />
      {s.label}
    </span>
  );
}
