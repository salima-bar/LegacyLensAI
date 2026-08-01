import type { ReactNode } from "react";
import { Bell, Search } from "lucide-react";

interface TopBarProps {
  title: string;
  subtitle?: string;
  right?: ReactNode;
}

export function TopBar({ title, subtitle, right }: TopBarProps) {
  return (
    <div
      style={{
        height: 60,
        flexShrink: 0,
        borderBottom: "1px solid var(--border)",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        padding: "0 24px",
      }}
    >
      <div>
        <div className="ll-display" style={{ fontSize: 15, fontWeight: 600 }}>{title}</div>
        {subtitle && <div style={{ fontSize: 12, color: "var(--text-3)" }}>{subtitle}</div>}
      </div>
      <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
        <div style={{ position: "relative", display: "flex", alignItems: "center" }}>
          <Search size={14} style={{ position: "absolute", left: 10, color: "var(--text-3)" }} />
          <input className="ll-input" placeholder="Search projects…" style={{ width: 220, padding: "7px 10px 7px 30px", borderRadius: 8, fontSize: 13 }} />
          <span className="ll-mono" style={{ position: "absolute", right: 8, fontSize: 10, color: "var(--text-3)", border: "1px solid var(--border)", padding: "1px 5px", borderRadius: 4 }}>⌘K</span>
        </div>
        {right}
        <div className="ll-rail-btn" style={{ width: 34, height: 34 }}>
          <Bell size={15} strokeWidth={1.8} />
        </div>
        <div
          style={{
            width: 30,
            height: 30,
            borderRadius: "50%",
            background: "linear-gradient(135deg,#e8a33d,#b8632e)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontSize: 12,
            fontWeight: 700,
            color: "#17120a",
            fontFamily: "var(--font-display)",
          }}
        >
          SL
        </div>
      </div>
    </div>
  );
}
