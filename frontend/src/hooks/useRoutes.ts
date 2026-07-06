import { useState } from "react";

import { optimizeRoute } from "../api/routes";

export default function useRoutes() {

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState<any>(null);

    const [error, setError] = useState("");

    async function optimize(
        source: string,
        destination: string,
        algorithm: string,
    ) {

        setLoading(true);

        setError("");

        setResult(null);

        try {

            const response = await optimizeRoute({

                source,

                destination,

                algorithm,

            });

            setResult(response);

            return response;

        } catch (err: any) {

            console.error(err);

            const message =
                err.response?.data?.detail ||
                err.response?.data?.message ||
                "Unable to optimize route.";

            setError(message);

            return null;

        } finally {

            setLoading(false);

        }

    }

    function clearResult() {

        setResult(null);

        setError("");

    }

    return {

        loading,

        result,

        error,

        optimize,

        clearResult,

    };

}