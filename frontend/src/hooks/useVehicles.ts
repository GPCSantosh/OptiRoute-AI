import { useEffect, useState } from "react";
import { getVehicles } from "../api/vehicles";

export default function useVehicles() {

    const [vehicles, setVehicles] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function load() {

            try {

                const data = await getVehicles();
                
                setVehicles(data);

            } finally {

                setLoading(false);

            }

        }

        load();

    }, []);

    return {
        vehicles,
        loading,
    };

}