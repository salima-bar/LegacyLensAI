interface ScoreRingProps {
  score: number;
  size?: number;
  stroke?: number;
}

export function ScoreRing({ score, size = 56, stroke = 5 }: ScoreRingProps) {
  const r = (size - stroke) / 2;
  const c = 2 * Math.PI * r;
  const color = score >= 75 ? "var(--green)" : score >= 45 ? "var(--accent)" : "var(--red)";

  return (
    <div style={{ position: "relative", width: size, height: size }}>
      <svg width={size} height={size} style={{ transform: "rotate(-90deg)" }}>
        <circle cx={size / 2} cy={size / 2} r={r} stroke="var(--border)" strokeWidth={stroke} fill="none" />
        <circle
          cx={size / 2}
          cy={size / 2}
          r={r}
          stroke={color}
          strokeWidth={stroke}
          fill="none"
          strokeDasharray={c}
          strokeDashoffset={c - (score / 100) * c}
          strokeLinecap="round"
        />
      </svg>
      <div
        className="ll-mono"
        style={{ position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 13, fontWeight: 600, color: "var(--text)" }}
      >
        {score}
      </div>
    </div>
  );
}
