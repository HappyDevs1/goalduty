import axios from "axios";
import { localBaseUrl } from "../utils/serverUrl";

const API_BASE_URL = `${localBaseUrl}/ai`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const transScribeAudio = async (audioFile: File) => {
  const formData = new FormData();
  formData.append("audio", audioFile);

  try {
    const response = await api.post("/transcribe", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error transcribing audio:", error);
    throw error;
  }
}

export const chatWithAI = async (user_id: number, message: string) => {
  try {
    const response = await api.post("/chat", { user_id, message });
    return response.data;
  } catch (error) {
    console.error("Error chatting with AI:", error);
    throw error;
  }
}

export const summarizeText = async (text: string) => {
  try {
    const response = await api.post("/summarize", { text });
    return response.data;
  } catch (error) {
    console.error("Error summarizing text:", error);
    throw error;
  }
}

export const generateDailyTasks = async (user_id: number) => {
  try {
    const response = await api.post("/daily-tasks", { user_id });
    return response.data;
  } catch (error) {
    console.error("Error generating daily tasks:", error);
    throw error;
  }
}

export const summarizeDailyTasks = async (user_id: number) => {
  try {
    const response = await api.post("/daily-tasks/summary", { user_id });
    return response.data;
  } catch (error) {
    console.error("Error summarizing daily tasks:", error);
    throw error;
  }
}