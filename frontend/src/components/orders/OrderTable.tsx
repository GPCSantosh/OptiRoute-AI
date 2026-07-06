import useOrders from "../../hooks/useOrders";
import { deleteOrder } from "../../api/orders";

type Props = {
    onEdit: (order: any) => void;
    search?: string;
};

export default function OrderTable({
    onEdit,
    search = "",
}: Props) {
    const { orders, loading } = useOrders();

    async function handleDelete(id: string) {
        const ok = window.confirm("Delete this order?");
        if (!ok) return;

        try {
            await deleteOrder(id);

            alert("Order deleted successfully.");

            window.location.reload();
        } catch (err: any) {
            console.error(err);

            alert(
                JSON.stringify(
                    err.response?.data ?? "Unable to delete order.",
                    null,
                    2
                )
            );
        }
    }

    if (loading) {
        return (
            <div
                style={{
                    padding: 40,
                    textAlign: "center",
                    fontSize: 18,
                    color: "#64748b",
                }}
            >
                Loading Orders...
            </div>
        );
    }

    const filtered = orders.filter((order: any) => {
        const q = search.toLowerCase();

        return (
            order.order_number
                ?.toString()
                .toLowerCase()
                .includes(q) ||

            order.customer_name
                ?.toLowerCase()
                .includes(q) ||

            order.customer_phone
                ?.toLowerCase()
                .includes(q)
        );
    });

    return (
        <div
            style={{
                background: "#fff",
                borderRadius: 14,
                overflow: "hidden",
                boxShadow: "0 8px 20px rgba(0,0,0,.08)",
            }}
        >
            <div
                style={{
                    overflowX: "auto",
                }}
            >
                <table
                    style={{
                        width: "100%",
                        minWidth: 1450,
                        borderCollapse: "collapse",
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
                            <th style={th}>Order No</th>
                            <th style={th}>Customer</th>
                            <th style={th}>Phone</th>
                            <th style={th}>Pickup Address</th>
                            <th style={th}>Delivery Address</th>
                            <th style={th}>Weight</th>
                            <th style={th}>Priority</th>
                            <th style={th}>Status</th>
                            <th style={th}>Distance</th>
                            <th style={th}>ETA</th>
                            <th style={th}>Actions</th>
                        </tr>
                    </thead>

                    <tbody>
                        {filtered.length === 0 ? (
                            <tr>
                                <td
                                    colSpan={12}
                                    style={{
                                        padding: 40,
                                        textAlign: "center",
                                        color: "#64748b",
                                    }}
                                >
                                    No Orders Found
                                </td>
                            </tr>
                        ) : (
                            filtered.map(
                                (
                                    order: any,
                                    index: number
                                ) => (
                                    <tr
                                        key={order.id}
                                        style={{
                                            borderBottom:
                                                "1px solid #e5e7eb",
                                        }}
                                    >
                                        <td style={td}>
                                            {index + 1}
                                        </td>

                                        <td style={td}>
                                            {order.order_number}
                                        </td>

                                        <td style={td}>
                                            {order.customer_name}
                                        </td>

                                        <td style={td}>
                                            {order.customer_phone}
                                        </td>

                                        <td style={td}>
                                            {order.pickup_address}
                                        </td>

                                        <td style={td}>
                                            {order.delivery_address}
                                        </td>

                                        <td style={td}>
                                            {order.package_weight} kg
                                        </td>

                                        <td style={td}>
                                            <span
                                                style={{
                                                    padding:
                                                        "6px 12px",
                                                    borderRadius: 20,
                                                    background:
                                                        order.priority ===
                                                        "HIGH"
                                                            ? "#fee2e2"
                                                            : "#fef3c7",
                                                    color:
                                                        order.priority ===
                                                        "HIGH"
                                                            ? "#b91c1c"
                                                            : "#92400e",
                                                    fontWeight: 600,
                                                }}
                                            >
                                                {order.priority}
                                            </span>
                                        </td>

                                        <td style={td}>
                                            <span
                                                style={{
                                                    padding:
                                                        "6px 12px",
                                                    borderRadius: 20,
                                                    background:
                                                        "#dbeafe",
                                                    color:
                                                        "#1d4ed8",
                                                    fontWeight: 600,
                                                }}
                                            >
                                                {order.status}
                                            </span>
                                        </td>

                                        <td style={td}>
                                            {order.estimated_distance}
                                        </td>

                                        <td style={td}>
                                            {order.estimated_time}
                                        </td>

                                        <td style={td}>
                                            <div
                                                style={{
                                                    display: "flex",
                                                    gap: 8,
                                                }}
                                            >
                                                <button
                                                    style={
                                                        editBtn
                                                    }
                                                    onClick={() =>
                                                        onEdit(
                                                            order
                                                        )
                                                    }
                                                >
                                                    Edit
                                                </button>

                                                <button
                                                    style={
                                                        deleteBtn
                                                    }
                                                    onClick={() =>
                                                        handleDelete(
                                                            order.id
                                                        )
                                                    }
                                                >
                                                    Delete
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                )
                            )
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

const th = {
    padding: "16px",
    textAlign: "left" as const,
    whiteSpace: "nowrap" as const,
};

const td = {
    padding: "16px",
    whiteSpace: "nowrap" as const,
};

const editBtn = {
    background: "#2563eb",
    color: "white",
    border: "none",
    borderRadius: 8,
    padding: "8px 16px",
    cursor: "pointer",
};

const deleteBtn = {
    background: "#ef4444",
    color: "white",
    border: "none",
    borderRadius: 8,
    padding: "8px 16px",
    cursor: "pointer",
};