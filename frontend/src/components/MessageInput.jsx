import { useState } from "react";

export default function MessageInput({ onSubmit }) {
  const [text, setText] = useState("");

  return (
    <div className="card">
      <h2>Enter SMS Message</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type your message..."
      />
      <button onClick={() => onSubmit(text)}>
        Check Spam
      </button>
    </div>
  );
}