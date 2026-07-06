import { useEffect, useState } from "react";

type Props = {
    open: boolean;
    mode: "add" | "edit";
    order?: any;
    onClose: () => void;
    onSave: (order: any) => void;
};

export default function OrderModal({
    open,
    mode,
    order,
    onClose,
    onSave,
}: Props) {

    const [form, setForm] = useState<any>({});

    useEffect(() => {

        if (!open) return;

        if (mode === "edit" && order) {

            setForm({
                ...order,
            });

        } else {

            setForm({
                order_number: "",
                customer_name: "",
                customer_phone: "",
                pickup_address: "",
                delivery_address: "",
                pickup_latitude: 0,
                pickup_longitude: 0,
                delivery_latitude: 0,
                delivery_longitude: 0,
                package_weight: 0,
                priority: "MEDIUM",
                status: "PENDING",
            });

        }

    }, [open, mode, order]);

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
                background: "rgba(15,23,42,.55)",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                zIndex: 999,
            }}
        >

            <div
                style={{
                    width: 760,
                    maxWidth: "96%",
                    background: "#fff",
                    borderRadius: 14,
                    padding: 30,
                    maxHeight: "90vh",
                    overflowY: "auto",
                    boxShadow: "0 20px 50px rgba(0,0,0,.25)",
                }}
            >

                <h2
                    style={{
                        marginTop: 0,
                        textAlign: "center",
                        color: "#1e293b",
                    }}
                >
                    {mode === "add"
                        ? "➕ Create Order"
                        : "✏️ Edit Order"}
                </h2>

                <p
                    style={{
                        textAlign: "center",
                        color: "#64748b",
                        marginBottom: 25,
                    }}
                >
                    {mode === "add"
                        ? "Fill the order details."
                        : `Order Number : ${form.order_number}`}
                </p>

                <label style={label}>Order Number</label>

                <input
                    name="order_number"
                    value={form.order_number || ""}
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

                <label style={label}>Customer Name</label>

                <input
                    name="customer_name"
                    value={form.customer_name || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Customer Phone</label>

                <input
                    name="customer_phone"
                    type="tel"
                    value={form.customer_phone || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Pickup Address</label>

                <input
                    name="pickup_address"
                    value={form.pickup_address || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>Delivery Address</label>

                <input
                    name="delivery_address"
                    value={form.delivery_address || ""}
                    onChange={change}
                    style={input}
                />

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns: "1fr 1fr",
                        gap: 20,
                    }}
                >

                    <div>

                        <label style={label}>
                            Pickup Latitude
                        </label>

                        <input
                            type="number"
                            name="pickup_latitude"
                            value={form.pickup_latitude}
                            onChange={change}
                            style={input}
                        />

                    </div>

                    <div>

                        <label style={label}>
                            Pickup Longitude
                        </label>

                        <input
                            type="number"
                            name="pickup_longitude"
                            value={form.pickup_longitude}
                            onChange={change}
                            style={input}
                        />

                    </div>

                    <div>

                        <label style={label}>
                            Delivery Latitude
                        </label>

                        <input
                            type="number"
                            name="delivery_latitude"
                            value={form.delivery_latitude}
                            onChange={change}
                            style={input}
                        />

                    </div>

                    <div>

                        <label style={label}>
                            Delivery Longitude
                        </label>

                        <input
                            type="number"
                            name="delivery_longitude"
                            value={form.delivery_longitude}
                            onChange={change}
                            style={input}
                        />

                    </div>

                </div>

                <label style={label}>
                    Package Weight (kg)
                </label>

                <input
                    type="number"
                    name="package_weight"
                    value={form.package_weight}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Priority
                </label>

                <select
                    name="priority"
                    value={form.priority}
                    onChange={change}
                    style={input}
                >
                    <option value="HIGH">HIGH</option>
                    <option value="MEDIUM">MEDIUM</option>
                </select>

                {mode === "edit" && (

                    <>
                        <label style={label}>
                            Status
                        </label>

                        <select
                            name="status"
                            value={form.status}
                            onChange={change}
                            style={input}
                        >
                            <option value="PENDING">
                                PENDING
                            </option>
                        </select>
                    </>

                )}

                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between",
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
                            ? "Create Order"
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
    padding: "12px 14px",
    borderRadius: 8,
    border: "1px solid #d1d5db",
    boxSizing: "border-box" as const,
};

const cancelBtn = {
    background: "#6b7280",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "10px 20px",
    cursor: "pointer",
};

const saveBtn = {
    background: "#2563eb",
    color: "#fff",
    border: "none",
    borderRadius: 8,
    padding: "10px 22px",
    cursor: "pointer",
    fontWeight: 600,
};