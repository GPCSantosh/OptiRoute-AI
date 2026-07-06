import { useState } from "react";

import RoadToolbar from "../components/roads/RoadToolbar";
import RoadTable from "../components/roads/RoadTable";
import RoadModal from "../components/roads/RoadModal";

import {
    createRoad,
    updateRoad,
} from "../api/roads";

export default function Roads() {

    const [open, setOpen] = useState(false);

    const [mode, setMode] = useState<"add" | "edit">("add");

    const [selectedRoad, setSelectedRoad] = useState<any>(null);

    const [search, setSearch] = useState("");

    const [refreshKey, setRefreshKey] = useState(0);

    function refresh() {
        setRefreshKey((prev) => prev + 1);
    }

    function handleAdd() {

        setMode("add");

        setSelectedRoad(null);

        setOpen(true);

    }

    function handleEdit(road: any) {

        setMode("edit");

        setSelectedRoad(road);

        setOpen(true);

    }

    async function handleSave(road: any) {

        try {

            if (mode === "add") {

                await createRoad(road);

                alert("Road created successfully.");

            } else {

                await updateRoad(
                    selectedRoad.id,
                    road
                );

                alert("Road updated successfully.");

            }

            setOpen(false);

            refresh();

        } catch (err: any) {

            console.error(err);

            console.log(err.response?.data);

            alert(

                JSON.stringify(

                    err.response?.data ??

                    "Unable to save road.",

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

            <RoadToolbar
                search={search}
                onSearch={setSearch}
                onAdd={handleAdd}
            />

            <RoadTable
                key={refreshKey}
                search={search}
                onEdit={handleEdit}
            />

            <RoadModal
                open={open}
                mode={mode}
                road={selectedRoad}
                onClose={() => setOpen(false)}
                onSave={handleSave}
            />

        </div>

    );

}