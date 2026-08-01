import { useEffect, useRef, useState } from "react";
import { Sparkles, Send } from "lucide-react";
import type { ChatMessage } from "@/types";

interface AssistantPanelProps {
  projectName: string;
}

const SUGGESTIONS = ["Explain this module", "Find security risks", "Draft a migration plan"];

export function AssistantPanel({ projectName }: AssistantPanelProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([
    { role: "ai", text: `I've indexed ${projectName}. Ask me about any module, risk, or design decision — I'll cite the file it came from.` },
  ]);
  const [input, setInput] = useState("");
  const endRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const send = () => {
    if (!input.trim()) return;
    setMessages((m) => [...m, { role: "user", text: input }]);
    setInput("");
    // Placeholder response — replace with a real API call once the assistant backend is wired in.
    setTimeout(() => {
      setMessages((m) => [...m, { role: "ai", text: "This is a placeholder response. Connect the assistant API to replace it." }]);
    }, 650);
  };

  return (
    <div
      style={{
        width: 360,
        flexShrink: 0,
        borderLeft: "1px solid var(--border)",
        display: "flex",
        flexDirection: "column",
        background: "var(--bg)",
      }}
    >
      <div style={{ padding: "16px 18px", borderBottom: "1px solid var(--border)", display: "flex", alignItems: "center", gap: 9 }}>
        <div className="ll-reticle" style={{ width: 18, height: 18, display: "flex", alignItems: "center", justifyContent: "center" }}>
          <Sparkles size={11} color="var(--accent)" />
        </div>
        <div>
          <div style={{ fontSize: 13, fontWeight: 600 }}>AI Assistant</div>
          <div className="ll-mono" style={{ fontSize: 10.5, color: "var(--text-3)" }}>Grounded in this codebase</div>
        </div>
      </div>

      <div className="ll-scrollable" style={{ flex: 1, overflowY: "auto", padding: 16, display: "flex", flexDirection: "column", gap: 12 }}>
        {messages.map((m, i) => (
          <div key={i} style={{ alignSelf: m.role === "user" ? "flex-end" : "flex-start", maxWidth: "88%" }}>
            <div
              className={m.role === "user" ? "ll-chat-bubble-user" : "ll-chat-bubble-ai"}
              style={{ padding: "10px 13px", borderRadius: 11, fontSize: 13, lineHeight: 1.55 }}
            >
              {m.text}
            </div>
          </div>
        ))}
        <div ref={endRef} />
      </div>

      <div style={{ padding: 14, borderTop: "1px solid var(--border)" }}>
        <div style={{ display: "flex", gap: 6, marginBottom: 10, flexWrap: "wrap" }}>
          {SUGGESTIONS.map((s) => (
            <button
              key={s}
              className="ll-btn"
              style={{ fontSize: 11, padding: "5px 9px", borderRadius: 6, background: "var(--surface-2)", color: "var(--text-2)", border: "1px solid var(--border)" }}
              onClick={() => setInput(s)}
            >
              {s}
            </button>
          ))}
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 8, background: "var(--surface-2)", border: "1px solid var(--border)", borderRadius: 10, padding: "6px 6px 6px 12px" }}>
          <input
            className="ll-input"
            style={{ flex: 1, background: "transparent", border: "none", fontSize: 13 }}
            placeholder="Ask about this codebase…"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && send()}
          />
          <button className="ll-btn ll-btn-primary" style={{ width: 30, height: 30, borderRadius: 7, padding: 0, justifyContent: "center" }} onClick={send}>
            <Send size={13} />
          </button>
        </div>
      </div>
    </div>
  );
}
