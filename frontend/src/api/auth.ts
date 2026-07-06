import axios from "./axios";

export async function login(email: string, password: string) {
    const response = await axios.post("/auth/login", {
        email,
        password,
    });

    return response.data;
}
export async function register(data: {
    first_name: string;
    last_name: string;
    username: string;
    email: string;
    password: string;
}) {
    const response = await axios.post(
        "/auth/register",
        data
    );

    return response.data;
}
export async function logout() {
    const token = localStorage.getItem("token");

    return axios.post(
        "/auth/logout",
        {},
        {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        }
    );
}

export async function me() {
    const token = localStorage.getItem("token");

    const response = await axios.get("/auth/me", {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    return response.data;
}