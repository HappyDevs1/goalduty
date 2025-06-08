"use client";

import React, { useState } from "react";
import CheckboxWithLabel from "../components/CheckboxWithLabel";

type Task = {
  id: string;
  label: string;
  checked: boolean;
};

const Tasks: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"non_negotiable" | "negotiable">("non_negotiable");

  const [tasks, setTasks] = useState<{
    non_negotiable: Task[];
    negotiable: Task[];
  }>({
    non_negotiable: [
      { id: "1", label: "Finish report", checked: false },
      { id: "2", label: "Email client", checked: false },
    ],
    negotiable: [
      { id: "3", label: "Buy groceries", checked: false },
      { id: "4", label: "Call mom", checked: false },
    ],
  });

  const handleCheckboxChange = (tab: "non_negotiable" | "negotiable", id: string, checked: boolean) => {
    setTasks((prev) => ({
      ...prev,
      [tab]: prev[tab].map((task) =>
        task.id === id ? { ...task, checked } : task
      ),
    }));
  };

  return (
    <div className="w-full max-w-md mx-auto p-4">
      {/* Tabs */}
      <div className="flex justify-around border-b mb-4">
        {(["non_negotiable", "negotiable"] as const).map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`py-2 px-4 font-medium capitalize ${
              activeTab === tab
                ? "border-b-2 border-blue-600 text-blue-600"
                : "text-gray-600 hover:text-blue-500"
            }`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Task List */}
      <div className="space-y-3">
        {tasks[activeTab].length === 0 ? (
          <p className="text-gray-500 text-center">No tasks available.</p>
        ) : (
          tasks[activeTab].map((task) => (
            <CheckboxWithLabel
              key={task.id}
              id={task.id}
              label={task.label}
              checked={task.checked}
              onChange={(checked) => handleCheckboxChange(activeTab, task.id, checked)}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default Tasks;
