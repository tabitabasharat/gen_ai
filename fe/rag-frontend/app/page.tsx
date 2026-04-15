import ChatWindow from "../components/ChatWindow";

export default function Home() {
  return (
    <main className="flex flex-col gap-3 items-center justify-center h-screen bg-gray-100">
        <h1 className="text-black font-bold">ChatBot AI (RAG)</h1>

      <ChatWindow />
    </main>
  );
}