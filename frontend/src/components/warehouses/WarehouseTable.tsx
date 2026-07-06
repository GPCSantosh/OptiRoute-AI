import { deleteWarehouse } from "../../api/warehouses";
import useWarehouses from "../../hooks/useWarehouses";

type Props = {
    onEdit: (warehouse: any) => void;
    search: string;
};

export default function WarehouseTable({
    onEdit,
    search,
}: Props) {

    const {
        warehouses,
        loading,
    } = useWarehouses();

    async function handleDelete(id: string) {

        const ok = window.confirm(
            "Delete this warehouse?"
        );

        if (!ok) return;

        try {

            await deleteWarehouse(id);

            alert("Warehouse deleted successfully.");

            window.location.reload();

        } catch (err: any) {

            console.error(err);

            alert(
                err.response?.data?.detail ??
                "Unable to delete warehouse."
            );

        }

    }

    if (loading) {

        return (
            <div
                style={{
                    textAlign: "center",
                    padding: 50,
                    fontSize: 18,
                    color: "#64748b",
                }}
            >
                Loading Warehouses...
            </div>
        );

    }

    const filtered = warehouses.filter((warehouse: any) => {

        const q = search.toLowerCase();

        return (

            warehouse.warehouse_code
                ?.toLowerCase()
                .includes(q) ||

            warehouse.warehouse_name
                ?.toLowerCase()
                .includes(q) ||

            warehouse.city
                ?.toLowerCase()
                .includes(q) ||

            warehouse.state
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
                boxShadow:
                    "0 8px 22px rgba(0,0,0,.08)",
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
                        minWidth: 1300,
                        borderCollapse: "collapse",
                    }}
                >

                    <thead>

                        <tr
                            style={{
                                background: "#1e293b",
                                color: "#fff",
                            }}
                        >

                            <th style={th}>#</th>

                            <th style={th}>Code</th>

                            <th style={th}>Warehouse</th>

                            <th style={th}>Address</th>

                            <th style={th}>City</th>

                            <th style={th}>State</th>

                            <th style={th}>Capacity</th>

                            <th style={th}>Available</th>

                            <th style={th}>Status</th>

                            <th style={th}>Actions</th>

                        </tr>

                    </thead>

                    <tbody>

                        {filtered.length === 0 ? (

                            <tr>

                                <td
                                    colSpan={10}
                                    style={{
                                        textAlign: "center",
                                        padding: 40,
                                        color: "#64748b",
                                    }}
                                >
                                    No Warehouses Found
                                </td>

                            </tr>

                        ) : (

                            filtered.map(
                                (
                                    warehouse: any,
                                    index: number
                                ) => (

                                    <tr
                                        key={warehouse.id}
                                        style={{
                                            borderBottom:
                                                "1px solid #e5e7eb",
                                        }}
                                    >

                                        <td style={td}>
                                            {index + 1}
                                        </td>

                                        <td style={td}>
                                            {warehouse.warehouse_code}
                                        </td>

                                        <td style={td}>
                                            {warehouse.warehouse_name}
                                        </td>

                                        <td style={td}>
                                            {warehouse.address}
                                        </td>

                                        <td style={td}>
                                            {warehouse.city}
                                        </td>

                                        <td style={td}>
                                            {warehouse.state}
                                        </td>

                                        <td style={td}>
                                            {warehouse.total_capacity}
                                        </td>

                                        <td style={td}>
                                            {warehouse.available_capacity}
                                        </td>

                                        <td style={td}>

                                            <span
                                                style={{
                                                    padding:
                                                        "6px 12px",
                                                    borderRadius: 20,
                                                    fontWeight: 600,
                                                    background:
                                                        warehouse.is_active
                                                            ? "#DCFCE7"
                                                            : "#FEE2E2",
                                                    color:
                                                        warehouse.is_active
                                                            ? "#166534"
                                                            : "#991B1B",
                                                }}
                                            >
                                                {warehouse.is_active
                                                    ? "ACTIVE"
                                                    : "INACTIVE"}
                                            </span>

                                        </td>

                                        <td style={td}>

                                            <div
                                                style={{
                                                    display: "flex",
                                                    gap: 8,
                                                }}
                                            >

                                                <button
                                                    style={editBtn}
                                                    onClick={() =>
                                                        onEdit(
                                                            warehouse
                                                        )
                                                    }
                                                >
                                                    Edit
                                                </button>

                                                <button
                                                    style={deleteBtn}
                                                    onClick={() =>
                                                        handleDelete(
                                                            warehouse.id
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
};

const td = {
    padding: "16px",
    whiteSpace: "nowrap" as const,
};

const editBtn = {
    background: "#2563EB",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "8px 16px",
    cursor: "pointer",
};

const deleteBtn = {
    background: "#EF4444",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "8px 16px",
    cursor: "pointer",
};