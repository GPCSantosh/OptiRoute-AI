import api from "./api";

export async function getOrders() {

    const response = await api.get("/orders/");

    return response.data;

}

export async function createOrder(data: any) {

    const response = await api.post("/orders/", data);

    return response.data;

}