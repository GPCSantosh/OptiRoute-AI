import { useEffect, useState } from "react";

import RouteOptimizerToolbar from "../components/routes/RouteOptimizerToolbar";
import RouteResultCard from "../components/routes/RouteResultCard";
import RoutePathTable from "../components/routes/RoutePathTable";
import RouteStatistics from "../components/routes/RouteStatistics";
import RouteMap from "../components/routes/RouteMap";

import useRoutes from "../hooks/useRoutes";

import { getWarehouses } from "../api/warehouses";

import GoogleMapComponent from "../components/GoogleMap";

export default function RouteOptimizer() {
    return (
        <div
            style={{
                padding: 20,
            }}
        >
            <h2>Route Optimizer</h2>

            <GoogleMapComponent />
        </div>
    );
}