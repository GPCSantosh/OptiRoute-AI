import { ReactNode } from "react";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

interface Props {
    children: ReactNode;
}

export default function DashboardLayout({
    children,
}: Props) {

    return (

        <div className="flex min-h-screen bg-gray-100">

            <Sidebar />

            <div className="flex-1">

                <Navbar />

                <main className="p-6">

                    {children}

                </main>

            </div>

        </div>

    );

}