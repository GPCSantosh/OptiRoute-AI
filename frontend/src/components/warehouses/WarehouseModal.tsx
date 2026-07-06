import { useEffect, useState } from "react";

type Props = {
    open: boolean;
    mode: "add" | "edit";
    warehouse?: any;
    onClose: () => void;
    onSave: (warehouse: any) => void;
};

export default function WarehouseModal({
    open,
    mode,
    warehouse,
    onClose,
    onSave,
}: Props) {
    const [form, setForm] = useState<any>({});

    useEffect(() => {
        if (!open) return;

        if (mode === "edit" && warehouse) {
            setForm({
                ...warehouse,
            });
        } else {
            setForm({
                warehouse_code: "",
                warehouse_name: "",
                address: "",
                city: "",
                state: "",
                latitude: 0,
                longitude: 0,
                total_capacity: 1000,
                available_capacity: 1000,
                is_active: true,
            });
        }
    }, [open, mode, warehouse]);

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
                    : type === "checkbox"
                    ? (e.target as HTMLInputElement).checked
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
                    width: 760,
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
                        color: "#0f172a",
                        textAlign: "center",
                    }}
                >
                    {mode === "add"
                        ? "🏬 Add Warehouse"
                        : "✏️ Edit Warehouse"}
                </h2>

                <p
                    style={{
                        textAlign: "center",
                        color: "#64748b",
                        marginBottom: 28,
                    }}
                >
                    {mode === "add"
                        ? "Enter warehouse information."
                        : `Warehouse : ${form.warehouse_code}`}
                </p>

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns:
                            "repeat(2,1fr)",
                        gap: 18,
                    }}
                >
                    <div>
                        <label style={label}>
                            Warehouse Code
                        </label>

                        <input
                            name="warehouse_code"
                            value={
                                form.warehouse_code || ""
                            }
                            onChange={change}
                            disabled={mode === "edit"}
                            style={{
                                ...input,
                                ...(mode === "edit"
                                    ? disabledStyle
                                    : {}),
                            }}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            Warehouse Name
                        </label>

                        <input
                            name="warehouse_name"
                            value={
                                form.warehouse_name || ""
                            }
                            onChange={change}
                            style={input}
                        />
                    </div>

                    <div
                        style={{
                            gridColumn: "1 / span 2",
                        }}
                    >
                        <label style={label}>
                            Address
                        </label>

                        <input
                            name="address"
                            value={
                                form.address || ""
                            }
                            onChange={change}
                            style={input}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            City
                        </label>

                        <input
                            name="city"
                            value={form.city || ""}
                            onChange={change}
                            style={input}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            State
                        </label>

                        <input
                            name="state"
                            value={form.state || ""}
                            onChange={change}
                            style={input}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            Latitude
                        </label>

                        <input
                            type="number"
                            step="0.000001"
                            name="latitude"
                            value={
                                form.latitude ?? 0
                            }
                            onChange={change}
                            disabled={mode === "edit"}
                            style={{
                                ...input,
                                ...(mode === "edit"
                                    ? disabledStyle
                                    : {}),
                            }}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            Longitude
                        </label>

                        <input
                            type="number"
                            step="0.000001"
                            name="longitude"
                            value={
                                form.longitude ?? 0
                            }
                            onChange={change}
                            disabled={mode === "edit"}
                            style={{
                                ...input,
                                ...(mode === "edit"
                                    ? disabledStyle
                                    : {}),
                            }}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            Total Capacity
                        </label>

                        <input
                            type="number"
                            name="total_capacity"
                            value={
                                form.total_capacity ?? 0
                            }
                            onChange={change}
                            disabled={mode === "edit"}
                            style={{
                                ...input,
                                ...(mode === "edit"
                                    ? disabledStyle
                                    : {}),
                            }}
                        />
                    </div>

                    <div>
                        <label style={label}>
                            Available Capacity
                        </label>

                        <input
                            type="number"
                            name="available_capacity"
                            value={
                                form.available_capacity ??
                                0
                            }
                            onChange={change}
                            style={input}
                        />
                    </div>

                    <div
                        style={{
                            gridColumn: "1 / span 2",
                        }}
                    >
                        <label style={label}>
                            Warehouse Status
                        </label>

                        <select
                            name="is_active"
                            value={
                                form.is_active
                                    ? "true"
                                    : "false"
                            }
                            onChange={(e) =>
                                setForm({
                                    ...form,
                                    is_active:
                                        e.target.value ===
                                        "true",
                                })
                            }
                            style={input}
                        >
                            <option value="true">
                                Active
                            </option>

                            <option value="false">
                                Inactive
                            </option>
                        </select>
                    </div>
                </div>

                <div
                    style={{
                        display: "flex",
                        justifyContent:
                            "flex-end",
                        gap: 12,
                        marginTop: 32,
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
                                id: warehouse?.id,
                            })
                        }
                        style={saveBtn}
                    >
                        {mode === "add"
                            ? "Create Warehouse"
                            : "Save Changes"}
                    </button>
                </div>
            </div>
        </div>
    );
}

const label = {
    display: "block",
    marginBottom: 6,
    marginTop: 12,
    fontWeight: 600,
    color: "#334155",
};

const input = {
    width: "100%",
    padding: "12px 14px",
    borderRadius: 8,
    border: "1px solid #CBD5E1",
    fontSize: 15,
    boxSizing: "border-box" as const,
};

const disabledStyle = {
    background: "#F1F5F9",
    cursor: "not-allowed",
};

const cancelBtn = {
    padding: "11px 20px",
    border: "none",
    borderRadius: 8,
    background: "#64748B",
    color: "#fff",
    cursor: "pointer",
};

const saveBtn = {
    padding: "11px 24px",
    border: "none",
    borderRadius: 8,
    background: "#2563EB",
    color: "#fff",
    cursor: "pointer",
    fontWeight: 600,
};