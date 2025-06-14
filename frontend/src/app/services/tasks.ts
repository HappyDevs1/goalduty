import axios from "axios";
import { localBaseUrl } from "../utils/serverUrl";

const API_BASE_URL = `${localBaseUrl}/daily_tasks`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const createTask = async (taskData: any) => {
  try {
    const response = await api.post("/daily_task", taskData);
    return response.data;
  } catch (error) {
    console.error("Error creating task:", error);
    throw error;
  }
};

export const getTask = async (taskId: string) => {
  try {
    const response = await api.get(`/daily_task/${taskId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching task:", error);
    throw error;
  }
};

export const updateTask = async (taskId: string, taskData: any) => {
  try {
    const response = await api.put(`/daily_task/${taskId}`, taskData);
    return response.data;
  } catch (error) {
    console.error("Error updating task:", error);
    throw error;
  }
};

export const deleteTask = async (taskId: string) => {
  try {
    const response = await api.delete(`/daily_task/${taskId}`);
    return response.data;
  } catch (error) {
    console.error("Error deleting task:", error);
    throw error;
  }
};

export const getAllTasks = async () => {
  try {
    const response = await api.get("/daily_task");
    return response.data;
  } catch (error) {
    console.error("Error fetching all tasks:", error);
    throw error;
  }
};