import axios from "axios";

const authConfig = () => ({
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export async function getRoads() {
    const response = await axios.get(
        "/roads",
        authConfig()
    );

    return response.data;
}

export async function getRoad(id: string) {
    const response = await axios.get(
        `/roads/${id}`,
        authConfig()
    );

    return response.data;
}

export async function createRoad(road: any) {
    const payload = {
        road_name: road.road_name,
        source: road.source,
        destination: road.destination,
        distance: Number(road.distance),
        travel_time: Number(road.travel_time),
    };

    const response = await axios.post(
        "/roads",
        payload,
        authConfig()
    );

    return response.data;
}

export async function updateRoad(
    id: string,
    road: any
) {
    const payload = {
        road_name: road.road_name,
        source: road.source,
        destination: road.destination,
        distance: Number(road.distance),
        travel_time: Number(road.travel_time),
        traffic_factor: Number(road.traffic_factor),
        closed: Boolean(road.closed),
    };

    const response = await axios.put(
        `/roads/${id}`,
        payload,
        authConfig()
    );

    return response.data;
}

export async function deleteRoad(id: string) {
    const response = await axios.delete(
        `/roads/${id}`,
        authConfig()
    );

    return response.data;
}