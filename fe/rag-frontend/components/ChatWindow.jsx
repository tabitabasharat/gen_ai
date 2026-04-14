"use client";

import { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import { sendMessage } from "../lib/api";

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);

const handleSend = async (text) => {
  const userMsg = { text, sender: "user" };
  setMessages((prev) => [...prev, userMsg]);

  try {
    const res = await sendMessage(text);

    console.log("Backend response:", res);

    const botMsg = {
      text: res.answer.answer,   // ✅ FIX HERE
      sender: "bot",
    };

    setMessages((prev) => [...prev, botMsg]);

  } catch (error) {
    console.error(error);

    setMessages((prev) => [
      ...prev,
      { text: "Server error", sender: "bot" },
    ]);
  }
};

  return (
    <div className="flex flex-col h-[80vh] w-full max-w-2xl mx-auto border rounded-xl shadow-lg">
      <div className="flex-1 overflow-y-auto p-4 flex flex-col">
        {messages.map((msg, i) => (
          <MessageBubble key={i} text={msg.text} sender={msg.sender} />
        ))}
      </div>

      <ChatInput className="text-black" onSend={handleSend} />
    </div>
  );
}
