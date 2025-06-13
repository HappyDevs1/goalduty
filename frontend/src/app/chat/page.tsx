"use client";

import ChatComponent from "../components/ChatComponent";

export default function ChatPage() {
  return (
    <div className="flex flex-col h-screen justify-end px-4 py-2 bg-gray-100">
      <h1 className="text-xl font-semibold mb-4">Chat Page</h1>
      <ChatComponent />
    </div>
  );
}
