import { NavLink } from "react-router-dom";

export default function Sidebar() {

    return (

        <aside className="w-64 bg-slate-900 text-white">

            <div className="text-2xl font-bold p-6">

                OptiRoute AI

            </div>

            <nav className="flex flex-col">

                <NavLink className="p-4 hover:bg-slate-700" to="/">
                    Dashboard
                </NavLink>

                <NavLink className="p-4 hover:bg-slate-700" to="/vehicles">
                    Vehicles
                </NavLink>

                <NavLink className="p-4 hover:bg-slate-700" to="/orders">
                    Orders
                </NavLink>

                <NavLink className="p-4 hover:bg-slate-700" to="/warehouses">
                    Warehouses
                </NavLink>

                <NavLink className="p-4 hover:bg-slate-700" to="/analytics">
                    Analytics
                </NavLink>

                <NavLink className="p-4 hover:bg-slate-700" to="/routes">
                    Route Optimizer
                </NavLink>

            </nav>

        </aside>

    );

}