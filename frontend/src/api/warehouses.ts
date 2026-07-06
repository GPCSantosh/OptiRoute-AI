import axios from "./axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function getWarehouses() {
    const response = await axios.get(
        "/warehouses",
        authConfig()
    );

    return response.data;
}

export async function createWarehouse(
    warehouse: any
) {
    const response = await axios.post(
        "/warehouses",
        warehouse,
        authConfig()
    );

    return response.data;
}

export async function updateWarehouse(
    id: string,
    warehouse: any
) {
    const response = await axios.put(
        `/warehouses/${id}`,
        warehouse,
        authConfig()
    );

    return response.data;
}

export async function deleteWarehouse(
    id: string
) {
    const response = await axios.delete(
        `/warehouses/${id}`,
        authConfig()
    );

    return response.data;
}