import { useEffect, useState } from "react";
import { getDashboard } from "../api/dashboard";

export default function useDashboard() {
    const [data, setData] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<any>(null);

    useEffect(() => {
        async function load() {
            try {
                const result = await getDashboard();
                console.log("Dashboard API:", result);
                setData(result);
            } catch (err) {
                console.error(err);
                setError(err);
            } finally {
                setLoading(false);
            }
        }

        load();
    }, []);

    return {
        data,
        loading,
        error,
    };
}