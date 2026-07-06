import axios from "./axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function getOrders() {

    const response = await axios.get(
        "/orders",
        authConfig()
    );

    return response.data;

}

export async function createOrder(order: any) {

    const response = await axios.post(
        "/orders",
        order,
        authConfig()
    );

    return response.data;

}

export async function updateOrder(
    id: string,
    order: any
) {

    const response = await axios.put(
        `/orders/${id}`,
        order,
        authConfig()
    );

    return response.data;

}

export async function deleteOrder(
    id: string
) {

    const response = await axios.delete(
        `/orders/${id}`,
        authConfig()
    );

    return response.data;

}