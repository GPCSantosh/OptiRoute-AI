import useDrivers from "../../hooks/useDrivers";
import { deleteDriver } from "../../api/drivers";

type Props = {
    onEdit: (driver: any) => void;
};

export default function DriverTable({
    onEdit,
}: Props) {
    const {
        drivers,
        loading,
    } = useDrivers();

    async function handleDelete(id: string) {
        const ok = window.confirm(
            "Are you sure you want to delete this driver?"
        );

        if (!ok) return;

        try {
            await deleteDriver(id);

            alert("Driver deleted successfully.");

            window.location.reload();
        } catch (error: any) {
            console.error(error);

            alert(
                error.response?.data?.detail ||
                    "Unable to delete driver."
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
                Loading Drivers...
            </div>
        );
    }

    return (
        <div
            style={{
                width: "100%",
                background: "#fff",
                borderRadius: 14,
                overflow: "hidden",
                boxShadow: "0 8px 24px rgba(0,0,0,.08)",
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
                        minWidth: "1100px",
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
                            <th style={th}>Employee ID</th>
                            <th style={th}>First Name</th>
                            <th style={th}>Last Name</th>
                            <th style={th}>Phone</th>
                            <th style={th}>Email</th>
                            <th style={th}>License</th>
                            <th style={th}>Experience</th>
                            <th style={th}>Status</th>
                            <th style={th}>Rating</th>
                            <th style={th}>Actions</th>
                        </tr>
                    </thead>

                    <tbody>
                        {drivers.length === 0 ? (
                            <tr>
                                <td
                                    colSpan={11}
                                    style={{
                                        padding: 40,
                                        textAlign: "center",
                                        color: "#64748b",
                                    }}
                                >
                                    No drivers found.
                                </td>
                            </tr>
                        ) : (
                            drivers.map(
                                (
                                    driver: any,
                                    index: number
                                ) => (
                                    <tr
                                        key={driver.id}
                                        style={{
                                            borderBottom:
                                                "1px solid #e5e7eb",
                                        }}
                                    >
                                        <td style={td}>
                                            {index + 1}
                                        </td>

                                        <td style={td}>
                                            {driver.employee_id}
                                        </td>

                                        <td style={td}>
                                            {driver.first_name}
                                        </td>

                                        <td style={td}>
                                            {driver.last_name}
                                        </td>

                                        <td style={td}>
                                            {driver.phone}
                                        </td>

                                        <td style={td}>
                                            {driver.email}
                                        </td>

                                        <td style={td}>
                                            {driver.license_number}
                                        </td>

                                        <td style={td}>
                                            {
                                                driver.years_of_experience
                                            }{" "}
                                            Years
                                        </td>

                                        <td style={td}>
                                            <span
                                                style={{
                                                    padding:
                                                        "6px 12px",
                                                    borderRadius: 20,
                                                    background:
                                                        driver.status ===
                                                        "AVAILABLE"
                                                            ? "#dcfce7"
                                                            : driver.status ===
                                                              "ON_DELIVERY"
                                                            ? "#dbeafe"
                                                            : driver.status ===
                                                              "ON_BREAK"
                                                            ? "#fef3c7"
                                                            : "#fee2e2",
                                                    color:
                                                        "#111827",
                                                    fontWeight: 600,
                                                    fontSize: 13,
                                                }}
                                            >
                                                {driver.status}
                                            </span>
                                        </td>

                                        <td style={td}>
                                            {driver.rating ??
                                                "-"}
                                        </td>

                                        <td style={td}>
                                            <div
                                                style={{
                                                    display:
                                                        "flex",
                                                    gap: 8,
                                                }}
                                            >
                                                <button
                                                    style={
                                                        editBtn
                                                    }
                                                    onClick={() =>
                                                        onEdit(
                                                            driver
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
                                                            driver.id
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
    fontWeight: 700,
    whiteSpace: "nowrap" as const,
};

const td = {
    padding: "15px 16px",
    color: "#374151",
    whiteSpace: "nowrap" as const,
};

const editBtn = {
    background: "#2563eb",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "8px 14px",
    cursor: "pointer",
    fontWeight: 600,
};

const deleteBtn = {
    background: "#ef4444",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "8px 14px",
    cursor: "pointer",
    fontWeight: 600,
};