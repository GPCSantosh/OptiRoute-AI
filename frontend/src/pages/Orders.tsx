import { useState } from "react";

import OrderToolbar from "../components/orders/OrderToolbar";
import OrderTable from "../components/orders/OrderTable";
import OrderModal from "../components/orders/OrderModal";

import {
    createOrder,
    updateOrder,
} from "../api/orders";

export default function Orders() {

    const [open, setOpen] = useState(false);

    const [mode, setMode] = useState<"add" | "edit">("add");

    const [selectedOrder, setSelectedOrder] = useState<any>(null);

    const [search, setSearch] = useState("");

    const [refreshKey, setRefreshKey] = useState(0);

    function refresh() {
        setRefreshKey((prev) => prev + 1);
    }

    function handleAdd() {

        setMode("add");

        setSelectedOrder(null);

        setOpen(true);

    }

    function handleEdit(order: any) {

        setMode("edit");

        setSelectedOrder(order);

        setOpen(true);

    }

    async function handleSave(order: any) {

        try {

            if (mode === "add") {

                await createOrder(order);

                alert("Order created successfully.");

            } else {

                await updateOrder(
                    selectedOrder.id,
                    order
                );

                alert("Order updated successfully.");

            }

            setOpen(false);

            refresh();

        } catch (err: any) {

            console.error(err);

            console.log(err.response?.data);

            alert(

                JSON.stringify(

                    err.response?.data ??

                    "Unable to save order.",

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

            <OrderToolbar

                onAdd={handleAdd}

                onSearch={setSearch}

            />

            <OrderTable

                key={refreshKey}

                onEdit={handleEdit}

                search={search}

            />

            <OrderModal

                open={open}

                mode={mode}

                order={selectedOrder}

                onClose={() => setOpen(false)}

                onSave={handleSave}

            />

        </div>

    );

}