import { Outlet } from "react-router-dom";
import { Sidebar } from "./Sidebar";

/**
 * Permanent authenticated shell. The Sidebar is always visible here;
 * individual pages decide whether they render a TopBar (Dashboard,
 * Projects, Settings) or a custom header (Analysis).
 */
export function AppShell() {
  return (
    <div className="ll-root">
      <div style={{ height: "100vh", display: "flex" }}>
        <Sidebar />
        <div style={{ flex: 1, display: "flex", flexDirection: "column", minWidth: 0 }}>
          <Outlet />
        </div>
      </div>
    </div>
  );
}
