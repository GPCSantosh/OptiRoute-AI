import { useEffect, useState } from "react";

import { getDrivers } from "../api/drivers";

export default function useDrivers() {

    const [drivers, setDrivers] = useState<any[]>([]);

    const [loading, setLoading] = useState(true);

    async function loadDrivers() {

        try {

            const data = await getDrivers();

            setDrivers(data);

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        loadDrivers();

    }, []);

    return {

        drivers,

        loading,

        refreshDrivers: loadDrivers,

    };

}