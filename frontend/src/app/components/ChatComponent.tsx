"use client";

import { Plus, Send } from 'lucide-react';

export default function ChatComponent() {
  return (
    <div>
      {/* Chat Input Area */}
      <div className="flex items-end gap-2 border border-gray-300 rounded-full p-2 bg-white shadow-sm w-full max-w-3xl mx-auto">
        {/* Plus Button */}
        <button className="p-2 rounded-full hover:bg-gray-200 transition-colors">
          <Plus size={20} />
        </button>

        {/* Text Area that grows */}
        <textarea
          rows={1}
          placeholder="Type your message..."
          className="flex-1 self-center resize-none overflow-hidden border-none outline-none bg-transparent text-sm placeholder-gray-500"
          onInput={(e) => {
            const target = e.target as HTMLTextAreaElement;
            target.style.height = "auto"; // reset height
            target.style.height = `${target.scrollHeight}px`; // grow with content
          }}
        />

        {/* Send Button */}
        <button className="p-2 rounded-full hover:bg-blue-100 text-blue-600 transition-colors">
          <Send size={20} />
        </button>
      </div>
    </div>
  )
}