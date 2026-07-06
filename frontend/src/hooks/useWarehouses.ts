import { useEffect, useState } from "react";
import { getWarehouses } from "../api/warehouses";

export default function useWarehouses() {
    const [warehouses, setWarehouses] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);

    async function loadWarehouses() {
        try {
            const data = await getWarehouses();
            setWarehouses(data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        loadWarehouses();
    }, []);

    return {
        warehouses,
        loading,
        reload: loadWarehouses,
    };
}