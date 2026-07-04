import api from "./api";

export async function getWarehouses() {

    const response = await api.get("/warehouses/");

    return response.data;

}

export async function createWarehouse(data: any) {

    const response = await api.post("/warehouses/", data);

    return response.data;

}