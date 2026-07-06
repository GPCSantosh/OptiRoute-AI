import DashboardCard from "../../components/DashboardCard";
import useDashboard from "../../hooks/useDashboard";

export default function Dashboard() {

    const {
        data,
        loading,
        error,
    } = useDashboard();

    if (loading) {
        return <h2>Loading...</h2>;
    }

    if (error) {
        return <h2>API Error</h2>;
    }

    return (
        <>
            <h1>Dashboard</h1>

            <div
                style={{
                    display: "flex",
                    gap: 20,
                    flexWrap: "wrap",
                }}
            >
                <DashboardCard
                    title="Vehicles"
                    value={data.vehicles}
                    color="#2563eb"
                />

                <DashboardCard
                    title="Moving"
                    value={data.moving}
                    color="#16a34a"
                />

                <DashboardCard
                    title="Average Speed"
                    value={`${data.average_speed} km/h`}
                    color="#f97316"
                />

                <DashboardCard
                    title="Average Fuel"
                    value={`${data.average_fuel}%`}
                    color="#9333ea"
                />
            </div>
        </>
    );
}