"use client";

import React, { useState, useEffect } from "react";
import { getGoalsByUser } from "../services/goals";

type Goal = {
  name: string;
};

export default function Feedback() {
  const [goals, setGoals] = useState<Goal[]>([]);

  const handleFetchGoals = async () => {
    try {
      const user = localStorage.getItem("user");
      const userId = user ? JSON.parse(user).id : "";

      const goalsResponse = await getGoalsByUser(userId);
;
      setGoals(goalsResponse.data);
    } catch (error) {
      console.error("Error fetching goals:", error);
    }
  };

  useEffect(() => {
    handleFetchGoals();
  }, []);

  const formatGoalText = (text: string) => {
    const steps = text.split(/\d+\.\s|\*\*/).filter(Boolean);

    return (
      <div className="space-y-4">
        {steps.map((step, index) => {
          const trimmed = step.trim();

          if (trimmed === "") return null;

          // If it's the intro paragraph
          if (index === 0) {
            return (
              <p key={index} className="text-gray-700 leading-relaxed">
                {trimmed}
              </p>
            );
          }

          // Handle steps
          const splitIndex = trimmed.indexOf(":");
          const hasColon = splitIndex !== -1;
          const title = hasColon ? trimmed.slice(0, splitIndex).trim() : "";
          const desc = hasColon ? trimmed.slice(splitIndex + 1).trim() : trimmed;

          return (
            <div key={index}>
              {title && (
                <p className="font-bold text-gray-800 mb-1">{title}</p>
              )}
              <p className="text-gray-600 leading-relaxed">{desc}</p>
            </div>
          );
        })}
      </div>
    );
  };

  return (
    <div className="flex flex-col my-5">
      <h1 className="text-2xl font-bold mb-2">Action Steps</h1>
      {goals.length > 0 ? (
        <div className="space-y-6">
          {goals.map((goal, index) => (
            <div key={index} className="bg-white p-4 rounded shadow">
              {formatGoalText(goal.name)}
            </div>
          ))}
        </div>
      ) : (
        <span className="text-gray-600">No goals found.</span>
      )}
    </div>
  );
}