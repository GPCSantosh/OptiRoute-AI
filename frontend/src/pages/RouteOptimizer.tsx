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
                background: "white",
                color: "black",
                minHeight: "100vh",
            }}
        >
            <h1>Route Optimizer Loaded</h1>

            <p>If you can read this, React is rendering.</p>
        </div>
    );
}