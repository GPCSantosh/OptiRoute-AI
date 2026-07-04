import { useVehicles } from "../../hooks/useVehicles";
import VehicleRow from "./VehicleRow";

export default function VehicleTable() {

    const { data, isLoading } = useVehicles();

    if (isLoading) {
        return <h2>Loading...</h2>;
    }

    return (

        <div className="bg-white rounded-xl shadow">

            <table className="w-full">

                <thead className="bg-gray-100">

                    <tr>

                        <th className="p-4 text-left">Vehicle</th>

                        <th>Registration</th>

                        <th>Capacity</th>

                        <th>Fuel</th>

                        <th>Status</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {Array.isArray(data) &&
                        data.map((vehicle: any) => (
                            <VehicleRow
                                key={vehicle.id}
                                vehicle={vehicle}
                            />
                        ))}

                </tbody>

            </table>

        </div>

    );

}