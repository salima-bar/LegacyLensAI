import type { LucideIcon } from "lucide-react";

interface TabPlaceholderProps {
  label: string;
  icon: LucideIcon;
}

/**
 * Placeholder content for an Analysis tab. The reusable layout
 * (AnalysisLayout) is complete; tab content is intentionally not
 * implemented yet and will be built out per tab.
 */
export function TabPlaceholder({ label, icon: Icon }: TabPlaceholderProps) {
  return (
    <div
      className="ll-card-dashed ll-fade-up"
      style={{
        padding: "48px 24px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: 12,
        textAlign: "center",
        minHeight: 240,
      }}
    >
      <div style={{ width: 34, height: 34, borderRadius: 9, background: "var(--surface-2)", border: "1px solid var(--border)", display: "flex", alignItems: "center", justifyContent: "center" }}>
        <Icon size={16} color="var(--text-3)" />
      </div>
      <div style={{ fontSize: 13.5, fontWeight: 600, color: "var(--text-2)" }}>{label} content not implemented yet</div>
      <div className="ll-mono" style={{ fontSize: 11.5, color: "var(--text-3)", maxWidth: 320 }}>
        This tab renders through the reusable Analysis layout. Its content will be built out next.
      </div>
    </div>
  );
}
