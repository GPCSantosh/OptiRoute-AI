import api from "./api";

export async function getVehicles() {

    const response = await api.get("/vehicles/");

    return response.data;

}

export async function createVehicle(data: any) {

    const response = await api.post("/vehicles/", data);

    return response.data;

}