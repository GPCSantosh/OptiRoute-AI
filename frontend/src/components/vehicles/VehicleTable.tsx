import { useState } from "react";
import VehicleModal from "./VehicleModal";
import { updateVehicle, deleteVehicle } from "../../api/vehicles";
import useVehicles from "../../hooks/useVehicles";

export default function VehicleTable() {

    const { vehicles, loading } = useVehicles();
    const [open, setOpen] = useState(false);
    const [selectedVehicle, setSelectedVehicle] = useState<any>(null);
    async function handleDelete(id: string) {

        const ok = window.confirm(
            "Delete this vehicle?"
        );

        if (!ok) return;

        try {

            await deleteVehicle(id);

            alert("Vehicle deleted successfully.");

            window.location.reload();

        } catch (error) {

            console.error(error);

            alert("Unable to delete vehicle.");

        }

    }
    async function handleSave(vehicle: any) {

        try {

            await updateVehicle(
                vehicle.id,
                vehicle
            );

            alert("Vehicle updated successfully.");

            setOpen(false);

            window.location.reload();

        } catch (error) {

            console.error(error);

            alert("Update failed.");

        }

    }

    if (loading) {
        return <h2>Loading vehicles...</h2>;
    }

    return (
    <>
            <table
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                    background: "white",
                    borderRadius: 12,
                    overflow: "hidden",
                }}
            >
                <thead>
                    <tr
                        style={{
                            background: "#1e293b",
                            color: "white",
                        }}
                    >
                        <th style={th}>#</th>
                        <th style={th}>Registration</th>
                        <th style={th}>Vehicle</th>
                        <th style={th}>Manufacturer</th>
                        <th style={th}>Fuel</th>
                        <th style={th}>Status</th>
                        <th style={th}>Fuel</th>
                        <th style={th}>Actions</th>
                    </tr>
                </thead>

                <tbody>
                    {vehicles.map((vehicle: any, index: number) => (
                        <tr key={vehicle.id}>
                            <td style={td}>{index + 1}</td>

                            <td style={td}>
                                {vehicle.registration_number}
                            </td>

                            <td style={td}>
                                {vehicle.vehicle_name}
                            </td>

                            <td style={td}>
                                {vehicle.manufacturer}
                            </td>

                            <td style={td}>
                                {vehicle.fuel_type}
                            </td>

                            <td style={td}>
                                {vehicle.status}
                            </td>

                            <td style={td}>
                                {vehicle.current_fuel} L
                            </td>

                            <td style={td}>
                                <button
                                    style={editBtn}
                                    onClick={() => {
                                        setSelectedVehicle(vehicle);
                                        setOpen(true);
                                    }}
                                >
                                    Edit
                                </button>

                                <button
                                    style={deleteBtn}
                                    onClick={() => handleDelete(vehicle.id)}
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <VehicleModal
                open={open}
                vehicle={selectedVehicle}
                mode="edit"
                onClose={() => setOpen(false)}
                onSave={handleSave}
            />
        </>
    );

}

const th = {
    padding: 14,
    textAlign: "left" as const,
};

const td = {
    padding: 14,
    borderBottom: "1px solid #ddd",
};

const editBtn = {
    background: "#2563eb",
    color: "white",
    border: "none",
    padding: "7px 14px",
    marginRight: 8,
    borderRadius: 6,
    cursor: "pointer",
};

const deleteBtn = {
    background: "#ef4444",
    color: "white",
    border: "none",
    padding: "7px 14px",
    borderRadius: 6,
    cursor: "pointer",
};

