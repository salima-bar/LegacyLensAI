import { BookOpen } from "lucide-react";
import { TabPlaceholder } from "@/features/analysis/TabPlaceholder";

export function DocumentationTab() {
  return <TabPlaceholder label="Documentation" icon={BookOpen} />;
}
