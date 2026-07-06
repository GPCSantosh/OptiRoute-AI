import { useEffect, useState } from "react";

import { getOrders } from "../api/orders";

export default function useOrders() {

    const [orders, setOrders] = useState<any[]>([]);

    const [loading, setLoading] = useState(true);

    async function loadOrders() {

        try {

            const data = await getOrders();

            setOrders(data);

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        loadOrders();

    }, []);

    return {

        orders,

        loading,

        refreshOrders: loadOrders,

    };

}