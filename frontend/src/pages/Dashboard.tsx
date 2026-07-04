import DashboardLayout from "../layouts/DashboardLayout";
import DashboardCard from "../components/DashboardCard";
import { useDashboard } from "../hooks/useDashboard";

export default function Dashboard() {

    const {

        vehicles,

        orders,

        warehouses,

        loading,

    } = useDashboard();

    if (loading) {

        return (

            <DashboardLayout>

                <h2 className="text-2xl font-bold">

                    Loading Dashboard...

                </h2>

            </DashboardLayout>

        );

    }

    return (

        <DashboardLayout>

            <h1 className="text-3xl font-bold mb-6">

                Dashboard

            </h1>

            <div className="grid grid-cols-4 gap-5">

                <DashboardCard
                    title="Vehicles"
                    value={vehicles.data?.length ?? 0}
                />

                <DashboardCard
                    title="Orders"
                    value={orders.data?.length ?? 0}
                />

                <DashboardCard
                    title="Warehouses"
                    value={warehouses.data?.length ?? 0}
                />

                <DashboardCard
                    title="Drivers"
                    value="Coming Soon"
                />

            </div>

        </DashboardLayout>

    );

}