import { useState } from "react";

import DriverToolbar from "../components/drivers/DriverToolbar";
import DriverTable from "../components/drivers/DriverTable";
import DriverModal from "../components/drivers/DriverModal";

import {
    createDriver,
    updateDriver,
} from "../api/drivers";

export default function Drivers() {
    const [open, setOpen] = useState(false);

    const [mode, setMode] = useState<"add" | "edit">("add");

    const [selectedDriver, setSelectedDriver] = useState<any>(null);

    const [refreshKey, setRefreshKey] = useState(0);

    function refresh() {
        setRefreshKey((prev) => prev + 1);
    }

    function handleAdd() {
        setMode("add");
        setSelectedDriver(null);
        setOpen(true);
    }

    function handleEdit(driver: any) {
        setMode("edit");
        setSelectedDriver(driver);
        setOpen(true);
    }

    async function handleSave(driver: any) {
        try {
            if (mode === "add") {
                await createDriver(driver);
                alert("Driver created successfully.");
            } else {
                await updateDriver(
                    selectedDriver.id,
                    driver
                );

                alert("Driver updated successfully.");
            }

            setOpen(false);

            refresh();

        } catch (err: any) {
            console.error(err);

            alert(
                JSON.stringify(
                    err.response?.data ??
                        "Unable to save driver.",
                    null,
                    2
                )
            );
        }
    }

    return (
        <div
            style={{
                width: "100%",
                padding: "28px",
                boxSizing: "border-box",
            }}
        >
            <DriverToolbar
                onAdd={handleAdd}
            />

            <DriverTable
                key={refreshKey}
                onEdit={handleEdit}
            />

            <DriverModal
                open={open}
                mode={mode}
                driver={selectedDriver}
                onClose={() => setOpen(false)}
                onSave={handleSave}
            />
        </div>
    );
}