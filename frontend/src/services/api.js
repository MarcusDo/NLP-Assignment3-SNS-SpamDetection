import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", 
});

export const predictSpam = (message) => {
  return API.post("/predict", { message });
};