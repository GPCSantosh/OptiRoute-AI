import useRoads from "../../hooks/useRoads";
import { deleteRoad } from "../../api/roads";

type Props = {
    search: string;
    onEdit: (road: any) => void;
};

export default function RoadTable({
    search,
    onEdit,
}: Props) {

    const {
        roads,
        loading,
    } = useRoads();

    async function handleDelete(id: string) {

        const ok = window.confirm(
            "Delete this road?"
        );

        if (!ok) return;

        try {

            await deleteRoad(id);

            alert("Road deleted successfully.");

            window.location.reload();

        } catch (err: any) {

            console.error(err);

            alert(
                err.response?.data?.detail ??
                "Unable to delete road."
            );

        }

    }

    if (loading)
        return (
            <h2
                style={{
                    textAlign: "center",
                    padding: 40,
                }}
            >
                Loading Roads...
            </h2>
        );

    const filtered = roads.filter((road: any) => {

        const q = search.toLowerCase();

        return (

            road.road_name
                ?.toLowerCase()
                .includes(q) ||

            road.source
                ?.toLowerCase()
                .includes(q) ||

            road.destination
                ?.toLowerCase()
                .includes(q)

        );

    });

    return (

        <div
            style={{
                background: "white",
                borderRadius: 12,
                overflow: "hidden",
                boxShadow:
                    "0 8px 18px rgba(0,0,0,.08)",
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
                        minWidth: 1100,
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

                            <th style={th}>Road</th>

                            <th style={th}>Source</th>

                            <th style={th}>Destination</th>

                            <th style={th}>Distance</th>

                            <th style={th}>Travel Time</th>

                            <th style={th}>Traffic</th>

                            <th style={th}>Status</th>

                            <th style={th}>Actions</th>

                        </tr>

                    </thead>

                    <tbody>

                        {filtered.length === 0 ? (

                            <tr>

                                <td
                                    colSpan={9}
                                    style={{
                                        padding: 40,
                                        textAlign: "center",
                                        color: "#64748b",
                                    }}
                                >
                                    No Roads Found
                                </td>

                            </tr>

                        ) : (

                            filtered.map(
                                (
                                    road: any,
                                    index: number
                                ) => (

                                    <tr
                                        key={road.id}
                                        style={{
                                            borderBottom:
                                                "1px solid #e5e7eb",
                                        }}
                                    >

                                        <td style={td}>
                                            {index + 1}
                                        </td>

                                        <td style={td}>
                                            {road.road_name}
                                        </td>

                                        <td style={td}>
                                            {road.source}
                                        </td>

                                        <td style={td}>
                                            {road.destination}
                                        </td>

                                        <td style={td}>
                                            {road.distance} km
                                        </td>

                                        <td style={td}>
                                            {road.travel_time} min
                                        </td>

                                        <td style={td}>

                                            <span
                                                style={{
                                                    background:
                                                        "#fef3c7",
                                                    color:
                                                        "#92400e",
                                                    padding:
                                                        "6px 12px",
                                                    borderRadius: 20,
                                                    fontWeight: 600,
                                                }}
                                            >
                                                {road.traffic_factor}×
                                            </span>

                                        </td>

                                        <td style={td}>

                                            <span
                                                style={{
                                                    background:
                                                        road.closed
                                                            ? "#fee2e2"
                                                            : "#dcfce7",
                                                    color:
                                                        road.closed
                                                            ? "#b91c1c"
                                                            : "#166534",
                                                    padding:
                                                        "6px 12px",
                                                    borderRadius: 20,
                                                    fontWeight: 600,
                                                }}
                                            >
                                                {road.closed
                                                    ? "Closed"
                                                    : "Open"}
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
                                                            road
                                                        )
                                                    }
                                                >
                                                    Edit
                                                </button>

                                                <button
                                                    style={deleteBtn}
                                                    onClick={() =>
                                                        handleDelete(
                                                            road.id
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