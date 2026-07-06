import { useEffect, useState } from "react";

type Props = {
    open: boolean;
    mode: "add" | "edit";
    road?: any;
    onClose: () => void;
    onSave: (road: any) => void;
};

export default function RoadModal({
    open,
    mode,
    road,
    onClose,
    onSave,
}: Props) {

    const [form, setForm] = useState<any>({});

    useEffect(() => {

        if (!open) return;

        if (mode === "edit" && road) {

            setForm({
                ...road,
            });

        } else {

            setForm({
                road_name: "",
                source: "",
                destination: "",
                distance: 0,
                travel_time: 0,
                traffic_factor: 1,
                closed: false,
            });

        }

    }, [open, mode, road]);

    if (!open) return null;

    function change(
        e: React.ChangeEvent<
            HTMLInputElement | HTMLSelectElement
        >
    ) {

        const { name, value, type } = e.target;

        setForm({

            ...form,

            [name]:
                type === "number"
                    ? Number(value)
                    : value,

        });

    }

    return (

        <div
            style={{
                position: "fixed",
                inset: 0,
                background: "rgba(15,23,42,.55)",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                zIndex: 999,
                padding: 20,
            }}
        >

            <div
                style={{
                    width: 700,
                    maxWidth: "100%",
                    background: "#fff",
                    borderRadius: 14,
                    padding: 30,
                    maxHeight: "90vh",
                    overflowY: "auto",
                    boxShadow:
                        "0 20px 45px rgba(0,0,0,.25)",
                }}
            >

                <h2
                    style={{
                        margin: 0,
                        textAlign: "center",
                        color: "#0f172a",
                    }}
                >
                    {mode === "add"
                        ? "🛣 Add Road"
                        : "✏ Edit Road"}
                </h2>

                <p
                    style={{
                        textAlign: "center",
                        color: "#64748b",
                        marginBottom: 28,
                    }}
                >
                    {mode === "add"
                        ? "Create a new road."
                        : `Editing ${form.road_name}`}
                </p>

                <label style={label}>
                    Road Name
                </label>

                <input
                    name="road_name"
                    value={form.road_name || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Source
                </label>

                <input
                    name="source"
                    value={form.source || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Destination
                </label>

                <input
                    name="destination"
                    value={form.destination || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Distance (KM)
                </label>

                <input
                    type="number"
                    name="distance"
                    value={form.distance}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Travel Time (Minutes)
                </label>

                <input
                    type="number"
                    name="travel_time"
                    value={form.travel_time}
                    onChange={change}
                    style={input}
                />

                {mode === "edit" && (

                    <>

                        <label style={label}>
                            Traffic Factor
                        </label>

                        <input
                            type="number"
                            step="0.1"
                            name="traffic_factor"
                            value={
                                form.traffic_factor
                            }
                            onChange={change}
                            style={input}
                        />

                        <label style={label}>
                            Road Status
                        </label>

                        <select
                            value={
                                form.closed
                                    ? "closed"
                                    : "open"
                            }
                            onChange={(e) =>
                                setForm({

                                    ...form,

                                    closed:
                                        e.target.value ===
                                        "closed",

                                })
                            }
                            style={input}
                        >

                            <option value="open">
                                🟢 Open
                            </option>

                            <option value="closed">
                                🔴 Closed
                            </option>

                        </select>

                    </>

                )}

                <div
                    style={{
                        display: "flex",
                        justifyContent:
                            "flex-end",
                        gap: 12,
                        marginTop: 30,
                    }}
                >

                    <button
                        onClick={onClose}
                        style={cancelBtn}
                    >
                        Cancel
                    </button>

                    <button
                        onClick={() =>
                            onSave({

                                ...form,

                                id: road?.id,

                            })
                        }
                        style={saveBtn}
                    >
                        {mode === "add"
                            ? "Create Road"
                            : "Save Changes"}
                    </button>

                </div>

            </div>

        </div>

    );

}

const label = {
    display: "block",
    marginTop: 14,
    marginBottom: 6,
    fontWeight: 600,
    color: "#334155",
};

const input = {
    width: "100%",
    padding: "12px 14px",
    borderRadius: 8,
    border: "1px solid #CBD5E1",
    boxSizing: "border-box" as const,
};

const cancelBtn = {
    background: "#64748B",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "11px 22px",
    cursor: "pointer",
};

const saveBtn = {
    background: "#2563EB",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "11px 24px",
    cursor: "pointer",
    fontWeight: 600,
};