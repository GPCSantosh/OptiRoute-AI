import GoogleMapComponent from "../components/GoogleMap";

import RouteOptimizerToolbar from "../components/routes/RouteOptimizerToolbar";
import RouteResultCard from "../components/routes/RouteResultCard";
import RoutePathTable from "../components/routes/RoutePathTable";
import RouteStatistics from "../components/routes/RouteStatistics";

export default function RouteOptimizer() {
    return (
        <div
            style={{
                padding: 20,
            }}
        >
            <h2
                style={{
                    marginBottom: 20,
                }}
            >
                🚚 Route Optimizer
            </h2>

            {/* Toolbar */}

            <RouteOptimizerToolbar />

            <div
                style={{
                    marginTop: 25,
                    marginBottom: 25,
                }}
            >
                <GoogleMapComponent />
            </div>

            <RouteResultCard />

            <RouteStatistics />

            <RoutePathTable />
        </div>
    );
}