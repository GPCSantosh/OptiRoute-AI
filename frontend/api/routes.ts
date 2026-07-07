import axios from "axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function optimizeRoute(data: any) {
    const response = await axios.post(
        "/routes/optimize",
        data,
        authConfig()
    );

    return response.data;
}