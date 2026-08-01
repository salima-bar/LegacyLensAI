import { useNavigate } from "react-router-dom";
import { ArrowLeft, ArrowRight, Mail, Lock } from "lucide-react";
import { Logo } from "@/components/Logo";

export function Login() {
  const navigate = useNavigate();

  return (
    <div className="ll-root">
      <div style={{ height: "100vh", display: "flex", alignItems: "center", justifyContent: "center", position: "relative" }}>
        <div className="ll-bg-grid" style={{ position: "absolute", inset: 0, pointerEvents: "none" }} />
        <div className="ll-rail-btn" style={{ position: "absolute", top: 26, left: 32 }} onClick={() => navigate("/")}>
          <ArrowLeft size={16} />
        </div>
        <div className="ll-fade-up" style={{ position: "relative", width: 380 }}>
          <div style={{ display: "flex", justifyContent: "center", marginBottom: 26 }}><Logo /></div>
          <div className="ll-card" style={{ padding: 28 }}>
            <div className="ll-display" style={{ fontSize: 18, fontWeight: 600, marginBottom: 4, textAlign: "center" }}>Welcome back</div>
            <div style={{ fontSize: 13, color: "var(--text-2)", textAlign: "center", marginBottom: 22 }}>Log in to continue analyzing your codebases</div>

            <label style={{ display: "flex", flexDirection: "column", gap: 6, marginBottom: 14 }}>
              <span style={{ fontSize: 12, color: "var(--text-2)" }}>Email</span>
              <div style={{ position: "relative", display: "flex", alignItems: "center" }}>
                <Mail size={14} style={{ position: "absolute", left: 11, color: "var(--text-3)" }} />
                <input className="ll-input" defaultValue="sara@meridiansystems.io" style={{ width: "100%", padding: "10px 12px 10px 32px", borderRadius: 8, fontSize: 13 }} />
              </div>
            </label>
            <label style={{ display: "flex", flexDirection: "column", gap: 6, marginBottom: 20 }}>
              <span style={{ fontSize: 12, color: "var(--text-2)" }}>Password</span>
              <div style={{ position: "relative", display: "flex", alignItems: "center" }}>
                <Lock size={14} style={{ position: "absolute", left: 11, color: "var(--text-3)" }} />
                <input type="password" className="ll-input" defaultValue="••••••••••" style={{ width: "100%", padding: "10px 12px 10px 32px", borderRadius: 8, fontSize: 13 }} />
              </div>
            </label>
            <button className="ll-btn ll-btn-primary" style={{ width: "100%", justifyContent: "center", padding: "11px 0", borderRadius: 8, fontSize: 13.5, marginBottom: 12 }} onClick={() => navigate("/app")}>
              Continue <ArrowRight size={14} />
            </button>
            <button className="ll-btn ll-btn-ghost" style={{ width: "100%", justifyContent: "center", padding: "10px 0", borderRadius: 8, fontSize: 13 }} onClick={() => navigate("/app")}>
              Continue with SSO
            </button>
          </div>
          <div style={{ textAlign: "center", fontSize: 12, color: "var(--text-3)", marginTop: 16 }}>
            No account? <span style={{ color: "var(--accent)", cursor: "pointer" }}>Request access</span>
          </div>
        </div>
      </div>
    </div>
  );
}
