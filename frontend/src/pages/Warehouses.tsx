import { useState } from "react";

import WarehouseToolbar from "../components/warehouses/WarehouseToolbar";
import WarehouseTable from "../components/warehouses/WarehouseTable";
import WarehouseModal from "../components/warehouses/WarehouseModal";

import {
    createWarehouse,
    updateWarehouse,
} from "../api/warehouses";

export default function Warehouses() {

    const [open, setOpen] = useState(false);

    const [mode, setMode] = useState<"add" | "edit">("add");

    const [selectedWarehouse, setSelectedWarehouse] =
        useState<any>(null);

    const [search, setSearch] = useState("");

    const [refreshKey, setRefreshKey] = useState(0);

    function refresh() {
        setRefreshKey((prev) => prev + 1);
    }

    function handleAdd() {

        setMode("add");

        setSelectedWarehouse(null);

        setOpen(true);

    }

    function handleEdit(warehouse: any) {

        setMode("edit");

        setSelectedWarehouse(warehouse);

        setOpen(true);

    }

    async function handleSave(warehouse: any) {

        try {

            if (mode === "add") {

                await createWarehouse(warehouse);

                alert("Warehouse created successfully.");

            } else {

                await updateWarehouse(
                    selectedWarehouse.id,
                    warehouse
                );

                alert("Warehouse updated successfully.");

            }

            setOpen(false);

            refresh();

        } catch (err: any) {

            console.error(err);

            console.log(err.response?.data);

            alert(

                JSON.stringify(

                    err.response?.data ??

                    "Unable to save warehouse.",

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
                padding: 28,
                boxSizing: "border-box",
            }}
        >

            <WarehouseToolbar
                search={search}
                setSearch={setSearch}
                onAdd={handleAdd}
            />

            <WarehouseTable
                key={refreshKey}
                onEdit={handleEdit}
                search={search}
            />

            <WarehouseModal
                open={open}
                mode={mode}
                warehouse={selectedWarehouse}
                onClose={() => setOpen(false)}
                onSave={handleSave}
            />

        </div>

    );

}