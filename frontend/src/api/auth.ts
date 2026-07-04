import api from "./api";

export async function login(data: any) {

    const response = await api.post("/auth/login", data);

    return response.data;

}

export async function register(data: any) {

    const response = await api.post("/auth/register", data);

    return response.data;

}