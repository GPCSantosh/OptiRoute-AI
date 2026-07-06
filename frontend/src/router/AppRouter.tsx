import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom";

import Login from "../pages/auth/Login";
import Register from "../pages/auth/Register";

import Dashboard from "../pages/dashboard/Dashboard";
import Vehicles from "../pages/Vehicles";
import Drivers from "../pages/Drivers";
import Orders from "../pages/Orders";
import Warehouses from "../pages/Warehouses";
import Roads from "../pages/Roads";
import RouteOptimizer from "../pages/RouteOptimizer";
import Analytics from "../pages/Analytics";

import DashboardLayout from "../layouts/DashboardLayout";
import AuthLayout from "../layouts/AuthLayout";

import ProtectedRoute from "./ProtectedRoute";

export default function AppRouter() {

    return (

        <BrowserRouter>

            <Routes>

                {/* Authentication */}

                <Route element={<AuthLayout />}>

                    <Route
                        path="/"
                        element={<Login />}
                    />

                    <Route
                        path="/register"
                        element={<Register />}
                    />

                </Route>

                {/* Protected Routes */}

                <Route
                    element={
                        <ProtectedRoute>
                            <DashboardLayout />
                        </ProtectedRoute>
                    }
                >

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/vehicles"
                        element={<Vehicles />}
                    />

                    <Route
                        path="/drivers"
                        element={<Drivers />}
                    />

                    <Route
                        path="/orders"
                        element={<Orders />}
                    />

                    <Route
                        path="/warehouses"
                        element={<Warehouses />}
                    />

                    <Route
                        path="/roads"
                        element={<Roads />}
                    />

                    <Route
                        path="/route-optimizer"
                        element={<RouteOptimizer />}
                    />

                    <Route
                        path="/analytics"
                        element={<Analytics />}
                    />

                </Route>

            </Routes>

        </BrowserRouter>

    );

}