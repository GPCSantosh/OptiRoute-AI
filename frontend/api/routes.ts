import axios from "axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function optimizeRoute(payload: {
    source: string;
    destination: string;
    algorithm: string;
}) {

    const response = await axios.post(
        "/routes/optimize",
        payload,
        authConfig()
    );

    return response.data;

}