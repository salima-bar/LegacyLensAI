import { useNavigate } from "react-router-dom";
import { ScanSearch, ArrowRight, Sparkles, Layers, ShieldAlert, Map as MapIcon } from "lucide-react";
import { Logo } from "@/components/Logo";
import { ScoreRing } from "@/components/ScoreRing";
import { RISKS } from "@/data/mockData";

const FEATURES = [
  { icon: Layers, title: "Architecture, mapped", text: "LegacyLensAI traces every layer of your system and how it actually talks to itself — not what the diagram from 2011 says." },
  { icon: ShieldAlert, title: "Risks, ranked", text: "Security holes, dead dependencies, and untested modules surface first, ordered by what would actually hurt if it broke." },
  { icon: MapIcon, title: "A roadmap, not a report", text: "Get a phased modernization plan your team can execute, not a 40-page PDF that goes in a drawer." },
];

export function Landing() {
  const navigate = useNavigate();

  return (
    <div className="ll-root">
      <div className="ll-scrollable" style={{ height: "100vh", overflowY: "auto" }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "22px 40px" }}>
          <Logo />
          <div style={{ display: "flex", alignItems: "center", gap: 22 }}>
            <span style={{ fontSize: 13, color: "var(--text-2)", cursor: "pointer" }}>Product</span>
            <span style={{ fontSize: 13, color: "var(--text-2)", cursor: "pointer" }}>Pricing</span>
            <button className="ll-btn ll-btn-ghost" style={{ padding: "8px 15px", borderRadius: 7, fontSize: 13 }} onClick={() => navigate("/login")}>Log in</button>
          </div>
        </div>

        <div style={{ position: "relative", padding: "70px 40px 60px", textAlign: "center", overflow: "hidden" }}>
          <div className="ll-bg-grid" style={{ position: "absolute", inset: 0, top: -100, height: 520, pointerEvents: "none" }} />
          <div className="ll-glow" style={{ position: "absolute", top: 60, left: "50%", transform: "translateX(-50%)", width: 480, height: 260, pointerEvents: "none" }} />
          <div className="ll-fade-up" style={{ position: "relative" }}>
            <div className="ll-mono" style={{ display: "inline-flex", alignItems: "center", gap: 8, fontSize: 11.5, color: "var(--accent)", background: "var(--accent-soft)", border: "1px solid rgba(232,163,61,0.25)", padding: "5px 12px", borderRadius: 999, marginBottom: 26 }}>
              <ScanSearch size={12} /> Now reading COBOL, Java 6–8, .NET Framework, PHP 5
            </div>
            <h1 className="ll-display" style={{ fontSize: 54, fontWeight: 600, lineHeight: 1.08, maxWidth: 720, margin: "0 auto" }}>
              See through the legacy.
            </h1>
            <p style={{ fontSize: 16.5, color: "var(--text-2)", maxWidth: 520, margin: "22px auto 32px", lineHeight: 1.6 }}>
              Point LegacyLensAI at an old codebase and get its architecture, its risks, and a modernization roadmap — read and written by AI, in minutes instead of months.
            </p>
            <div style={{ display: "flex", gap: 10, justifyContent: "center" }}>
              <button className="ll-btn ll-btn-primary" style={{ padding: "11px 20px", borderRadius: 9, fontSize: 14 }} onClick={() => navigate("/login")}>
                Analyze a project <ArrowRight size={15} />
              </button>
              <button className="ll-btn ll-btn-ghost" style={{ padding: "11px 20px", borderRadius: 9, fontSize: 14 }}>See how it works</button>
            </div>
          </div>

          {/* Product preview */}
          <div className="ll-fade-up" style={{ marginTop: 56, maxWidth: 980, marginLeft: "auto", marginRight: "auto", textAlign: "left" }}>
            <div className="ll-card" style={{ padding: 0, overflow: "hidden", boxShadow: "0 40px 100px -30px rgba(0,0,0,0.6)" }}>
              <div style={{ display: "flex", alignItems: "center", gap: 8, padding: "11px 16px", borderBottom: "1px solid var(--border)" }}>
                <div style={{ display: "flex", gap: 6 }}>
                  {["#e2685d", "#e8a33d", "#4fae7c"].map((c) => <div key={c} style={{ width: 9, height: 9, borderRadius: "50%", background: c, opacity: 0.7 }} />)}
                </div>
                <span className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)", marginLeft: 6 }}>legacylens.ai/analysis/atlas-claims-engine</span>
              </div>
              <div style={{ display: "flex", padding: 20, gap: 16 }}>
                <div style={{ flex: 1.4 }}>
                  <div style={{ display: "flex", gap: 18, marginBottom: 16 }}>
                    <ScoreRing score={58} size={50} stroke={4} />
                    <div>
                      <div style={{ fontSize: 15, fontWeight: 600 }}>Atlas Claims Engine</div>
                      <div className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)", marginTop: 3 }}>.NET Framework 4.6 · SOAP · SQL Server</div>
                    </div>
                  </div>
                  <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                    {RISKS.slice(0, 3).map((r) => (
                      <div key={r.id} style={{ display: "flex", gap: 8, fontSize: 12, color: "var(--text-2)" }}>
                        <div style={{ width: 5, height: 5, borderRadius: "50%", background: r.sev === "critical" ? "var(--red)" : "var(--accent)", marginTop: 6, flexShrink: 0 }} />
                        {r.text}
                      </div>
                    ))}
                  </div>
                </div>
                <div style={{ flex: 1, background: "var(--surface-2)", borderRadius: 10, border: "1px solid var(--border)", padding: 14 }}>
                  <div style={{ display: "flex", alignItems: "center", gap: 7, marginBottom: 10 }}>
                    <Sparkles size={12} color="var(--accent)" />
                    <span style={{ fontSize: 12, fontWeight: 600 }}>AI Assistant</span>
                  </div>
                  <div className="ll-chat-bubble-ai" style={{ padding: "9px 11px", borderRadius: 9, fontSize: 11.5, lineHeight: 1.5 }}>
                    This module scores low mainly due to missing test coverage and direct stored-procedure calls.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div style={{ padding: "70px 40px", maxWidth: 1040, margin: "0 auto" }}>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 20 }}>
            {FEATURES.map((f) => (
              <div key={f.title} className="ll-fade-up">
                <div style={{ width: 34, height: 34, borderRadius: 9, background: "var(--accent-soft)", display: "flex", alignItems: "center", justifyContent: "center", marginBottom: 14 }}>
                  <f.icon size={16} color="var(--accent)" />
                </div>
                <div style={{ fontSize: 15, fontWeight: 600, marginBottom: 8 }}>{f.title}</div>
                <div style={{ fontSize: 13.5, color: "var(--text-2)", lineHeight: 1.65 }}>{f.text}</div>
              </div>
            ))}
          </div>
        </div>

        <div style={{ borderTop: "1px solid var(--border)", padding: "22px 40px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <Logo size={16} />
          <span className="ll-mono" style={{ fontSize: 11, color: "var(--text-3)" }}>© 2026 LegacyLensAI</span>
        </div>
      </div>
    </div>
  );
}
