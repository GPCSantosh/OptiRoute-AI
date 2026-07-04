import api from "./api";

export async function getAnalytics() {

    const response = await api.get("/analytics");

    return response.data;

}