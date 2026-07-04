import api from "./api";

export async function optimizeRoute(data: any) {

    const response = await api.post("/routes/optimize", data);

    return response.data;

}