import axios from "axios";
import { format } from "date-fns";

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const fetchNews = async (date = null) => {
  try {
    let params = {};
    if (date && date instanceof Date && !isNaN(date)) {
      params.date = format(date, "yyyy-MM-dd");
    }

    const response = await axios.get(`${API_BASE_URL}/news`, {
      params,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    });

    if (response.data?.status === "error") {
      throw new Error(response.data.message || "Erreur serveur");
    }

    return response.data?.data || [];
  } catch (error) {
    console.error("Error fetching news:", error);
    if (error.response?.status === 404) {
      return [];
    }
    throw new Error(
      error.message || "Erreur lors de la récupération des actualités"
    );
  }
};
