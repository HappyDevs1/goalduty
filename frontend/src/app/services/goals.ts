import axios from "axios";
import { localBaseUrl } from "../utils/serverUrl";

const API_BASE_URL = `${localBaseUrl}/future_goals`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const createGoal = async (goalData: any) => {
  try {
    const response = await api.post("/future_goal", goalData);
    return response.data;
  } catch (error) {
    console.error("Error creating goal:", error);
    throw error;
  }
};

export const getGoal = async (goalId: string) => {
  try {
    const response = await api.get(`/future_goal/${goalId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching goal:", error);
    throw error;
  }
};

export const updateGoal = async (goalId: string, goalData: any) => {
  try {
    const response = await api.put(`/future_goal/${goalId}`, goalData);
    return response.data;
  } catch (error) {
    console.error("Error updating goal:", error);
    throw error;
  }
};

export const deleteGoal = async (goalId: string) => {
  try {
    const response = await api.delete(`/future_goal/${goalId}`);
    return response.data;
  } catch (error) {
    console.error("Error deleting goal:", error);
    throw error;
  }
};

export const getAllGoals = async () => {
  try {
    const response = await api.get("/future_goal");
    return response.data;
  } catch (error) {
    console.error("Error fetching all goals:", error);
    throw error;
  }
};