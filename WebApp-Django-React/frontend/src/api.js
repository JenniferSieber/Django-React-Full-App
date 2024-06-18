import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// GET api url--using environment variable file --MUST START WITH VITE
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

api.interceptors.request.use(
  (config) => {
    // LOOK in local storage to see if we have an access token.
    // If there: add it as an authorization header request else nothing to do
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      // Authorization header for all requests from Frontend
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  // IF ERROR
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
