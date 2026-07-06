import { useEffect, useState } from "react";

type Props = {
    open: boolean;
    mode: "add" | "edit";
    vehicle?: any;
    onClose: () => void;
    onSave: (vehicle: any) => void;
};

export default function VehicleModal({
    open,
    mode,
    vehicle,
    onClose,
    onSave,
}: Props) {

    const [form, setForm] = useState<any>({});

    useEffect(() => {

        if (!open) return;

        if (mode === "edit" && vehicle) {

            setForm({ ...vehicle });

        } else {

            setForm({
                registration_number: "",
                vehicle_name: "",
                manufacturer: "",
                model: "",
                capacity_kg: 0,
                fuel_capacity: 0,
                current_fuel: 0,
                mileage: 0,
                max_speed: 0,
                fuel_type: "DIESEL",
            });

        }

    }, [open, vehicle, mode]);

    if (!open) return null;

    function change(
        e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
    ) {
        setForm({
            ...form,
            [e.target.name]:
                e.target.type === "number"
                    ? Number(e.target.value)
                    : e.target.value,
        });
    }

    return (
        <div
            style={{
                position: "fixed",
                inset: 0,
                background: "rgba(0,0,0,.45)",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                zIndex: 999,
            }}
        >
            <div
                style={{
                    width: 650,
                    background: "#fff",
                    borderRadius: 12,
                    padding: 30,
                    maxHeight: "90vh",
                    overflowY: "auto",
                }}
            >
                <p
                    style={{
                        textAlign: "center",
                        color: "#6b7280",
                        marginBottom: 25,
                    }}
                >
                    {mode === "add"
                        ? "Fill all vehicle information."
                        : `Registration Number: ${form.registration_number}`}
                </p>


                <label style={label}>
                    Registration Number
                </label>

                <input
                    name="registration_number"
                    value={form.registration_number || ""}
                    onChange={change}
                    disabled={mode === "edit"}
                    style={{
                        ...input,

                        ...(mode === "edit"
                            ? {
                                background: "#f3f4f6",
                                cursor: "not-allowed",
                            }
                            : {}),
                    }}
                />
                <label style={label}>Vehicle Name</label>

                <input
                    name="vehicle_name"
                    value={form.vehicle_name || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Manufacturer</label>

                <input
                    name="manufacturer"
                    value={form.manufacturer || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Model</label>

                <input
                    name="model"
                    value={form.model || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Fuel Type</label>

                <select
                    name="fuel_type"
                    value={form.fuel_type || ""}
                    onChange={change}
                    style={input}
                >
                    <option value="PETROL">PETROL</option>
                    <option value="DIESEL">DIESEL</option>
                    <option value="EV">EV</option>
                </select>

                <label style={label}>Fuel Remaining (L)</label>

                <input
                    type="number"
                    name="current_fuel"
                    value={form.current_fuel || 0}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Fuel Capacity (L)</label>

                <input
                    type="number"
                    name="fuel_capacity"
                    value={form.fuel_capacity || 0}
                    onChange={change}
                    style={input}
                />
                <label style={label}>
                    Mileage (km/L)
                </label>

                <input
                    type="number"
                    name="mileage"
                    value={form.mileage || 0}
                    onChange={change}
                    style={input}
                />
                <label style={label}>Vehicle Capacity (KG)</label>

                <input
                    type="number"
                    name="capacity_kg"
                    value={form.capacity_kg || 0}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Maximum Speed (Km/h)</label>

                <input
                    type="number"
                    name="max_speed"
                    value={form.max_speed || 0}
                    onChange={change}
                    style={input}
                />

                {mode === "edit" && (
                    <>
                        <label style={label}>Vehicle Status</label>

                        <select
                            name="status"
                            value={form.status || ""}
                            onChange={change}
                            style={input}
                        >
                            <option value="AVAILABLE">AVAILABLE</option>
                            <option value="IN_USE">IN USE</option>
                            <option value="MAINTENANCE">MAINTENANCE</option>
                            <option value="OUT_OF_SERVICE">OUT OF SERVICE</option>
                        </select>
                    </>
                )}

                <div
                    style={{
                        display: "flex",
                        justifyContent: "flex-end",
                        gap: 10,
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
                        onClick={() => onSave(form)}
                        style={saveBtn}
                    >
                        {mode === "add"
                            ? "Create Vehicle"
                            : "Save Changes"}
                    </button>
                </div>
            </div>
        </div>
    );
}

const label = {
    display: "block",
    marginTop: 16,
    marginBottom: 6,
    fontWeight: 600,
    color: "#374151",
};

const input = {
    width: "100%",
    padding: 12,
    borderRadius: 8,
    border: "1px solid #d1d5db",
    fontSize: 15,
    boxSizing: "border-box" as const,
};

const cancelBtn = {
    padding: "10px 20px",
    border: "none",
    borderRadius: 8,
    background: "#6b7280",
    color: "#fff",
    cursor: "pointer",
};

const saveBtn = {
    padding: "10px 22px",
    border: "none",
    borderRadius: 8,
    background: "#2563eb",
    color: "#fff",
    cursor: "pointer",
    fontWeight: 600,
};