import { useState } from "react";

import VehicleToolbar from "../components/vehicles/VehicleToolbar";
import VehicleTable from "../components/vehicles/VehicleTable";
import VehicleModal from "../components/vehicles/VehicleModal";

import { createVehicle } from "../api/vehicles";

export default function Vehicles() {

    const [open, setOpen] = useState(false);

    async function handleCreate(vehicle: any) {

        try {

            await createVehicle(vehicle);

            alert("Vehicle added successfully.");

            setOpen(false);

            window.location.reload();

        } catch (err: any) {

            console.error(err);

            alert(
                err.response?.data?.detail ||
                "Unable to create vehicle."
            );

        }

    }

    return (

        <>

            <VehicleToolbar
                onAdd={() => setOpen(true)}
            />

            <VehicleTable />

            <VehicleModal
                open={open}
                mode="add"
                onClose={() => setOpen(false)}
                onSave={handleCreate}
            />

        </>

    );

}