import { NavLink, useNavigate } from "react-router-dom";
import { LayoutGrid, FolderKanban, ScanSearch, Settings as SettingsIcon, LogOut } from "lucide-react";
import { Logo } from "./Logo";

const NAV_ITEMS = [
  { to: "/app", end: true, icon: LayoutGrid, label: "Dashboard" },
  { to: "/app/projects", end: false, icon: FolderKanban, label: "Projects" },
  { to: "/app/analysis", end: false, icon: ScanSearch, label: "Analysis" },
  { to: "/app/settings", end: false, icon: SettingsIcon, label: "Settings" },
];

export function Sidebar() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        width: 64,
        flexShrink: 0,
        borderRight: "1px solid var(--border)",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "18px 0",
        justifyContent: "space-between",
        background: "var(--bg)",
      }}
    >
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 22 }}>
        <div onClick={() => navigate("/")} style={{ cursor: "pointer" }} title="LegacyLensAI">
          <Logo showWord={false} size={20} />
        </div>
        <div style={{ display: "flex", flexDirection: "column", gap: 6, marginTop: 6 }}>
          {NAV_ITEMS.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className={({ isActive }) => `ll-rail-btn ${isActive ? "active" : ""}`}
              title={item.label}
            >
              <item.icon size={18} strokeWidth={1.8} />
            </NavLink>
          ))}
        </div>
      </div>
      <div className="ll-rail-btn" title="Log out" onClick={() => navigate("/")}>
        <LogOut size={17} strokeWidth={1.8} />
      </div>
    </div>
  );
}
