interface LogoProps {
  size?: number;
  showWord?: boolean;
}

export function Logo({ size = 22, showWord = true }: LogoProps) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
      <div
        className="ll-reticle"
        style={{ width: size, height: size, display: "flex", alignItems: "center", justifyContent: "center" }}
      >
        <div style={{ width: 6, height: 6, borderRadius: "50%", background: "var(--accent)" }} />
      </div>
      {showWord && (
        <span className="ll-display" style={{ fontSize: 15, fontWeight: 600, color: "var(--text)" }}>
          LegacyLens<span style={{ color: "var(--accent)" }}>AI</span>
        </span>
      )}
    </div>
  );
}
