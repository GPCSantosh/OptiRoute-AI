import axios from "./axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function getVehicles() {
    const response = await axios.get(
        "/vehicles",
        authConfig()
    );

    return response.data;
}

export async function createVehicle(vehicle: any) {
    const response = await axios.post(
        "/vehicles",
        vehicle,
        authConfig()
    );

    return response.data;
}

export async function updateVehicle(
    id: string,
    vehicle: any
) {
    const response = await axios.put(
        `/vehicles/${id}`,
        vehicle,
        authConfig()
    );

    return response.data;
}

export async function deleteVehicle(id: string) {
    const response = await axios.delete(
        `/vehicles/${id}`,
        authConfig()
    );

    return response.data;
}