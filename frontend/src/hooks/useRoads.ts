import { useEffect, useState } from "react";
import { getRoads } from "../api/roads";

export default function useRoads() {

    const [roads, setRoads] = useState<any[]>([]);

    const [loading, setLoading] = useState(true);

    async function loadRoads() {

        try {

            const data = await getRoads();

            setRoads(data);

        } catch (err) {

            console.error(err);

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        loadRoads();

    }, []);

    return {

        roads,

        loading,

        refreshRoads: loadRoads,

    };

}