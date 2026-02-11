import React, { useState } from "react";
import "../styles/chatbot.css";

const Chatbot = ({ skill, level }) => {
  const [messages, setMessages] = useState([
    { role: "luna", text: "Hi! I'm Luna. How can I help you learn today?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/luna/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_message: input,
          skill: skill,
          level: level,
        }),
      });

      const data = await response.json();
      setMessages((prev) => [...prev, { role: "luna", text: data.response }]);
    } catch (error) {
      setMessages((prev) => [...prev, { role: "luna", text: "Sorry, I'm having trouble connecting right now." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbot-window">
      <div className="chat-header">Luna AI Tutor ({level})</div>
      <div className="chat-messages">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="message luna">...</div>}
      </div>
      <div className="chat-input">
        <input 
          value={input} 
          onChange={(e) => setInput(e.target.value)} 
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Ask a question..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;