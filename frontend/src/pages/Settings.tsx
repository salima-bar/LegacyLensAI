import { useState } from "react";
import { Users, Boxes, Puzzle, KeyRound, Trash2, GitBranch, Plus, CircleAlert } from "lucide-react";
import { TopBar } from "@/components/TopBar";

type SectionKey = "profile" | "workspace" | "integrations" | "api" | "danger";

const SECTIONS: { key: SectionKey; label: string; icon: typeof Users }[] = [
  { key: "profile", label: "Profile", icon: Users },
  { key: "workspace", label: "Workspace", icon: Boxes },
  { key: "integrations", label: "Integrations", icon: Puzzle },
  { key: "api", label: "API keys", icon: KeyRound },
  { key: "danger", label: "Danger zone", icon: Trash2 },
];

export function Settings() {
  const [section, setSection] = useState<SectionKey>("profile");

  return (
    <>
      <TopBar title="Settings" subtitle="Account and workspace preferences" />
      <div className="ll-scrollable" style={{ flex: 1, overflowY: "auto", padding: "32px 36px 60px" }}>
        <div className="ll-display" style={{ fontSize: 22, fontWeight: 600, marginBottom: 22 }}>Settings</div>
        <div style={{ display: "flex", gap: 28 }}>
          <div style={{ width: 190, flexShrink: 0, display: "flex", flexDirection: "column", gap: 3 }}>
            {SECTIONS.map((s) => (
              <div
                key={s.key}
                onClick={() => setSection(s.key)}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 9,
                  padding: "8px 10px",
                  borderRadius: 7,
                  cursor: "pointer",
                  fontSize: 13,
                  color: section === s.key ? "var(--text)" : "var(--text-3)",
                  background: section === s.key ? "var(--surface-2)" : "transparent",
                }}
              >
                <s.icon size={14} /> {s.label}
              </div>
            ))}
          </div>
          <div style={{ flex: 1, maxWidth: 560 }}>
            {section === "profile" && (
              <div className="ll-card ll-fade-up" style={{ padding: 22, display: "flex", flexDirection: "column", gap: 16 }}>
                <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
                  <div style={{ width: 52, height: 52, borderRadius: "50%", background: "linear-gradient(135deg,#e8a33d,#b8632e)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 17, fontWeight: 700, color: "#17120a", fontFamily: "var(--font-display)" }}>SL</div>
                  <div>
                    <div style={{ fontSize: 14, fontWeight: 600 }}>Sara Lindqvist</div>
                    <div style={{ fontSize: 12, color: "var(--text-3)" }}>Principal Software Architect</div>
                  </div>
                </div>
                {[["Full name", "Sara Lindqvist"], ["Email", "sara@meridiansystems.io"], ["Role", "Software Architect"]].map(([l, v]) => (
                  <label key={l} style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                    <span style={{ fontSize: 12, color: "var(--text-2)" }}>{l}</span>
                    <input className="ll-input" defaultValue={v} style={{ padding: "9px 12px", borderRadius: 8, fontSize: 13 }} />
                  </label>
                ))}
                <button className="ll-btn ll-btn-primary" style={{ alignSelf: "flex-start", padding: "8px 16px", borderRadius: 8, fontSize: 13 }}>Save changes</button>
              </div>
            )}
            {section === "workspace" && (
              <div className="ll-card ll-fade-up" style={{ padding: 22, display: "flex", flexDirection: "column", gap: 16 }}>
                <label style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                  <span style={{ fontSize: 12, color: "var(--text-2)" }}>Workspace name</span>
                  <input className="ll-input" defaultValue="Meridian Systems" style={{ padding: "9px 12px", borderRadius: 8, fontSize: 13 }} />
                </label>
                <label style={{ display: "flex", flexDirection: "column", gap: 6 }}>
                  <span style={{ fontSize: 12, color: "var(--text-2)" }}>Default scan depth</span>
                  <select className="ll-input" style={{ padding: "9px 12px", borderRadius: 8, fontSize: 13 }}>
                    <option>Standard — architecture + risks</option>
                    <option>Deep — includes dependency graph</option>
                  </select>
                </label>
                <button className="ll-btn ll-btn-primary" style={{ alignSelf: "flex-start", padding: "8px 16px", borderRadius: 8, fontSize: 13 }}>Save changes</button>
              </div>
            )}
            {section === "integrations" && (
              <div className="ll-fade-up" style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                {["GitHub", "GitLab", "Bitbucket", "Jira"].map((n) => (
                  <div key={n} className="ll-card" style={{ padding: 14, display: "flex", alignItems: "center", justifyContent: "space-between" }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                      <GitBranch size={15} color="var(--text-2)" />
                      <span style={{ fontSize: 13 }}>{n}</span>
                    </div>
                    <button className="ll-btn ll-btn-ghost" style={{ padding: "6px 12px", borderRadius: 7, fontSize: 12 }}>Connect</button>
                  </div>
                ))}
              </div>
            )}
            {section === "api" && (
              <div className="ll-card ll-fade-up" style={{ padding: 22 }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 14 }}>
                  <span style={{ fontSize: 13, fontWeight: 600 }}>API keys</span>
                  <button className="ll-btn ll-btn-subtle" style={{ padding: "6px 12px", borderRadius: 7, fontSize: 12 }}><Plus size={12} /> New key</button>
                </div>
                <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "10px 0", borderTop: "1px solid var(--border-soft)" }}>
                  <span className="ll-mono" style={{ fontSize: 12.5, color: "var(--text-2)" }}>sk_live_••••••••wq3F</span>
                  <span className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)" }}>created Jun 12</span>
                </div>
              </div>
            )}
            {section === "danger" && (
              <div className="ll-card ll-fade-up" style={{ padding: 22, border: "1px solid rgba(226,104,93,0.3)" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                  <CircleAlert size={15} color="var(--red)" />
                  <span style={{ fontSize: 13, fontWeight: 600 }}>Delete workspace</span>
                </div>
                <p style={{ fontSize: 12.5, color: "var(--text-2)", marginBottom: 14, lineHeight: 1.6 }}>This permanently removes all projects, analyses, and history for Meridian Systems. This cannot be undone.</p>
                <button className="ll-btn" style={{ background: "var(--red-soft)", color: "var(--red)", padding: "8px 16px", borderRadius: 8, fontSize: 13 }}>Delete workspace</button>
              </div>
            )}
          </div>
        </div>
      </div>
    </>
  );
}
