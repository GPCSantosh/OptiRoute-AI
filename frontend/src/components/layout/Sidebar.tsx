import { NavLink } from "react-router-dom";

import {
    FaTruck,
    FaUserTie,
    FaWarehouse,
    FaRoute,
    FaChartPie,
    FaClipboardList,
    FaTachometerAlt,
    FaSignOutAlt,
} from "react-icons/fa";

import "../../styles/sidebar.css";

export default function Sidebar() {
    return (
        <aside className="sidebar">

            <div className="logo">
                OptiRoute
            </div>

            <nav>

                <NavLink to="/dashboard">
                    <FaTachometerAlt />
                    Dashboard
                </NavLink>

                <NavLink to="/vehicles">
                    <FaTruck />
                    Vehicles
                </NavLink>

                <NavLink to="/drivers">
                    <FaUserTie />
                    Drivers
                </NavLink>

                <NavLink to="/orders">
                    <FaClipboardList />
                    Orders
                </NavLink>

                <NavLink to="/warehouses">
                    <FaWarehouse />
                    Warehouses
                </NavLink>

                <NavLink to="/roads">
                    <FaRoute />
                    Roads
                </NavLink>

                <NavLink to="/route-optimizer">
                    <FaRoute />
                    🚚 Route Optimizer
                </NavLink>

                <NavLink to="/analytics">
                    <FaChartPie />
                    Analytics
                </NavLink>

            </nav>

            <button
                className="logout-btn"
                onClick={() => {

                    localStorage.removeItem("token");

                    window.location.href = "/";
                }}
            >
                <FaSignOutAlt />
                Logout
            </button>

        </aside>
    );
}