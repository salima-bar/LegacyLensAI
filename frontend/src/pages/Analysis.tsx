import { Navigate, Outlet, useParams } from "react-router-dom";
import { getProjectById } from "@/data/mockData";
import { AnalysisLayout } from "@/layouts/AnalysisLayout";

export function Analysis() {
  const { projectId } = useParams<{ projectId: string }>();
  const project = getProjectById(projectId);

  if (!project) {
    return <Navigate to="/app/projects" replace />;
  }

  return (
    <AnalysisLayout project={project}>
      <Outlet />
    </AnalysisLayout>
  );
}
