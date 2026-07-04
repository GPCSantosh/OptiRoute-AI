import { Routes, Route, Navigate } from "react-router-dom";

import Dashboard from "../pages/Dashboard";
import Vehicles from "../pages/Vehicles";
import Orders from "../pages/Orders";
import Warehouses from "../pages/Warehouses";
import Analytics from "../pages/Analytics";
import RouteOptimizer from "../pages/RouteOptimizer";

export default function AppRouter() {
    return (
        <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/vehicles" element={<Vehicles />} />
            <Route path="/orders" element={<Orders />} />
            <Route path="/warehouses" element={<Warehouses />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/routes" element={<RouteOptimizer />} />
            <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
    );
}