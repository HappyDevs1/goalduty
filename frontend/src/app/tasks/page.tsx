"use client";

import React, { useEffect, useState } from "react";
import CheckboxWithLabel from "../components/CheckboxWithLabel";
import { getTasksByUser } from "../services/tasks";

type Task = {
  id: string;
  label: string;
  checked: boolean;
};

const Tasks: React.FC = () => {
  const [activeTab, setActiveTab] = useState<"non_negotiable" | "negotiable">("non_negotiable");
  const [nonNegotiable, setNonNegotiable] = useState<Task[]>([]);
  const [negotiable, setNegotiable] = useState<Task[]>([]);

  const handleCheckboxChange = (
    tab: "non_negotiable" | "negotiable",
    id: string,
    checked: boolean
  ) => {
    if (tab === "non_negotiable") {
      setNonNegotiable((prev) =>
        prev.map((task) => (task.id === id ? { ...task, checked } : task))
      );
    } else {
      setNegotiable((prev) =>
        prev.map((task) => (task.id === id ? { ...task, checked } : task))
      );
    }
  };

const handleFetchTasks = async () => {
  try {
    const user = localStorage.getItem("user");
    const userId = user ? JSON.parse(user).id : "";

    const tasksResponse = await getTasksByUser(userId);

    const allTasks = tasksResponse.data;

    const nonNegotiableList: Task[] = [];
    const negotiableList: Task[] = [];

    allTasks.forEach((taskGroup: any) => {
      const nameObj = taskGroup.name;

      if (typeof nameObj === "object") {
        Object.entries(nameObj).forEach(([key, value], index) => {
          const flattenedTask: Task = {
            id: `${taskGroup.id}-${index}`, // unique ID per subtask
            label: value as string,
            checked: taskGroup.completed,
          };

          if (taskGroup.non_negotiable) {
            nonNegotiableList.push(flattenedTask);
          } else {
            negotiableList.push(flattenedTask);
          }
        });
      }
    });

    setNonNegotiable(nonNegotiableList);
    setNegotiable(negotiableList);
  } catch (error) {
    console.error("Error fetching tasks:", error);
  }
};


  useEffect(() => {
    handleFetchTasks();
  }, []);

  const currentTasks = activeTab === "non_negotiable" ? nonNegotiable : negotiable;

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
            {tab.replace("_", " ")}
          </button>
        ))}
      </div>

      {/* Task List */}
      <div className="space-y-3">
        {currentTasks.length === 0 ? (
          <p className="text-gray-500 text-center">No tasks available.</p>
        ) : (
          currentTasks.map((task) => (
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
