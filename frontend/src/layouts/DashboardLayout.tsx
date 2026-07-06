import React from "react";
import { Outlet } from "react-router-dom";

import Sidebar from "../components/layout/Sidebar";

import Navbar from "../components/layout/Navbar";

export default function DashboardLayout() {

    return (

        <>

            <Sidebar />

            <div
                style={{
                    marginLeft:260,
                    minHeight:"100vh",
                    background:"#f3f4f6"
                }}
            >

                <Navbar />

                <div
                    style={{
                        padding:30
                    }}
                >

                    <Outlet />

                </div>

            </div>

        </>

    );

}