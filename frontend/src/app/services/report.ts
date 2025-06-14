import axios from "axios";
import { localBaseUrl } from "../utils/serverUrl";

const API_BASE_URL = `${localBaseUrl}/daily_reports`;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const createReport = async (reportData: any) => {
  try {
    const response = await api.post("/daily_report", reportData);
    return response.data;
  } catch (error) {
    console.error("Error creating report:", error);
    throw error;
  }
};

export const getReport = async (reportId: string) => {
  try {
    const response = await api.get(`/daily_report/${reportId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching report:", error);
    throw error;
  }
};

export const updateReport = async (reportId: string, reportData: any) => {
  try {
    const response = await api.put(`/daily_report/${reportId}`, reportData);
    return response.data;
  } catch (error) {
    console.error("Error updating report:", error);
    throw error;
  }
};

export const deleteReport = async (reportId: string) => {
  try {
    const response = await api.delete(`/daily_report/${reportId}`);
    return response.data;
  } catch (error) {
    console.error("Error deleting report:", error);
    throw error;
  }
};

export const getAllReports = async () => {
  try {
    const response = await api.get("/daily_report");
    return response.data;
  } catch (error) {
    console.error("Error fetching all reports:", error);
    throw error;
  }
};