import axios from "./axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function getDrivers() {

    const response = await axios.get(
        "/drivers",
        authConfig()
    );

    return response.data;
}

export async function createDriver(driver: any) {

    const response = await axios.post(
        "/drivers",
        driver,
        authConfig()
    );

    return response.data;
}

export async function updateDriver(
    id: string,
    driver: any
) {

    const response = await axios.put(
        `/drivers/${id}`,
        driver,
        authConfig()
    );

    return response.data;
}

export async function deleteDriver(id: string) {

    const response = await axios.delete(
        `/drivers/${id}`,
        authConfig()
    );

    return response.data;
}