import axios from "axios";
import { localBaseUrl } from "../utils/serverUrl";

const API_BASE_URL = `${localBaseUrl}/journal`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const createJournalEntry = async (entryData: any) => {
  try {
    const response = await api.post("/journals", entryData);
    return response.data;
  } catch (error) {
    console.error("Error creating journal entry:", error);
    throw error;
  }
};

export const getJournalEntry = async (entryId: string) => {
  try {
    const response = await api.get(`/journals/${entryId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching journal entry:", error);
    throw error;
  }
}

export const updateJournalEntry = async (entryId: string, entryData: any) => {
  try {
    const response = await api.put(`/journals/${entryId}`, entryData);
    return response.data;
  } catch (error) {
    console.error("Error updating journal entry:", error);
    throw error;
  }
};

export const deleteJournalEntry = async (entryId: string) => {
  try {
    const response = await api.delete(`/journals/${entryId}`);
    return response.data;
  } catch (error) {
    console.error("Error deleting journal entry:", error);
    throw error;
  }
}

export const getAllJournalEntries = async () => {
  try {
    const response = await api.get("/journals");
    return response.data;
  } catch (error) {
    console.error("Error fetching all journal entries:", error);
    throw error;
  }
};