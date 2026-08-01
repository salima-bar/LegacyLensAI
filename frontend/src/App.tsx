import { Navigate, Route, Routes } from "react-router-dom";
import type { ReactNode } from "react";
import { AppShell } from "@/components/AppShell";
import { Landing } from "@/pages/Landing";
import { Login } from "@/pages/Login";
import { Dashboard } from "@/pages/Dashboard";
import { Projects } from "@/pages/Projects";
import { Analysis } from "@/pages/Analysis";
import { Settings } from "@/pages/Settings";
import { OverviewTab } from "@/features/analysis/tabs/OverviewTab";
import { DocumentationTab } from "@/features/analysis/tabs/DocumentationTab";
import { ArchitectureTab } from "@/features/analysis/tabs/ArchitectureTab";
import { RecommendationsTab } from "@/features/analysis/tabs/RecommendationsTab";
import { RoadmapTab } from "@/features/analysis/tabs/RoadmapTab";

const TOKEN_STORAGE_KEY = "legacylens_access_token";

function RequireAuth({ children }: { children: ReactNode }) {
  const token = typeof window !== "undefined" ? window.localStorage.getItem(TOKEN_STORAGE_KEY) : null;

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/login" element={<Login />} />

      <Route path="/app" element={<RequireAuth><AppShell /></RequireAuth>}>
        <Route index element={<Dashboard />} />
        <Route path="projects" element={<Projects />} />
        <Route path="settings" element={<Settings />} />

        <Route path="analysis/:projectId" element={<Analysis />}>
          <Route index element={<Navigate to="overview" replace />} />
          <Route path="overview" element={<OverviewTab />} />
          <Route path="documentation" element={<DocumentationTab />} />
          <Route path="architecture" element={<ArchitectureTab />} />
          <Route path="recommendations" element={<RecommendationsTab />} />
          <Route path="roadmap" element={<RoadmapTab />} />
        </Route>
      </Route>

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}
