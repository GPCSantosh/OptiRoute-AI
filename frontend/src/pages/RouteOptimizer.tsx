import { useEffect, useState } from "react";

import RouteOptimizerToolbar from "../components/routes/RouteOptimizerToolbar";
import RouteResultCard from "../components/routes/RouteResultCard";
import RoutePathTable from "../components/routes/RoutePathTable";
import RouteStatistics from "../components/routes/RouteStatistics";
import RouteMap from "../components/routes/RouteMap";

import useRoutes from "../hooks/useRoutes";

import { getWarehouses } from "../api/warehouses";

export default function RouteOptimizer() {

    const {

        loading,

        result,

        error,

        optimize,

    } = useRoutes();

    const [warehouses, setWarehouses] = useState<any[]>([]);

    const [source, setSource] = useState("");

    const [destination, setDestination] = useState("");

    const [algorithm, setAlgorithm] =
        useState("dijkstra");

    async function loadWarehouses() {

        try {

            const data = await getWarehouses();

            setWarehouses(data);

        } catch (err) {

            console.error(err);

            alert("Unable to load warehouses.");

        }

    }

    useEffect(() => {

        loadWarehouses();

    }, []);

    async function handleOptimize() {

        if (!source) {

            alert("Please select source warehouse.");

            return;

        }

        if (!destination) {

            alert("Please select destination warehouse.");

            return;

        }

        if (source === destination) {

            alert(
                "Source and destination cannot be the same."
            );

            return;

        }

        await optimize(

            source,

            destination,

            algorithm,

        );

    }

    return (

        <div
            style={{
                padding: 30,
                background: "#f8fafc",
                minHeight: "100vh",
            }}
        >

            <RouteOptimizerToolbar

                warehouses={warehouses}

                source={source}

                destination={destination}

                algorithm={algorithm}

                onSourceChange={setSource}

                onDestinationChange={setDestination}

                onAlgorithmChange={setAlgorithm}

                onOptimize={handleOptimize}

                loading={loading}

            />

            {error && (

                <div
                    style={{
                        background: "#fee2e2",
                        color: "#991b1b",
                        padding: 18,
                        borderRadius: 10,
                        marginBottom: 25,
                        fontWeight: 600,
                    }}
                >
                    ❌ {error}
                </div>

            )}

            <RouteResultCard

                result={result}

            />

            <RouteStatistics

                result={result}

            />

            <RoutePathTable

                result={result}

            />

            <RouteMap

                result={result}

            />

        </div>

    );

}