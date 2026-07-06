import axios from "./axios";

export async function getDashboard() {
    const response = await axios.get("/analytics/dashboard");
    return response.data;
}