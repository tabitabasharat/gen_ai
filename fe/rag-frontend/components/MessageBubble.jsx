export default function MessageBubble({ text, sender }) {
  return (
    <div
      className={`max-w-[75%] px-4 py-2 rounded-xl mb-2 ${
        sender === "user"
          ? "bg-blue-500 text-white self-end"
          : "bg-gray-200 text-black self-start"
      }`}
    >
      {text}
    </div>
  );
}

