import { useEffect, useState } from "react";

type Props = {
    open: boolean;
    mode: "add" | "edit";
    driver?: any;
    onClose: () => void;
    onSave: (driver: any) => void;
};

export default function DriverModal({
    open,
    mode,
    driver,
    onClose,
    onSave,
}: Props) {

    const [form, setForm] = useState<any>({});

    useEffect(() => {

        if (!open) return;

        if (mode === "edit" && driver) {

            setForm({
                employee_id: driver.employee_id,
                first_name: driver.first_name,
                last_name: driver.last_name,
                email: driver.email,
                phone: driver.phone,
                license_number: driver.license_number,
                years_of_experience: driver.years_of_experience,
                status: driver.status,
                rating: driver.rating,
            });

        } else {

            setForm({
                employee_id: "",
                first_name: "",
                last_name: "",
                email: "",
                phone: "",
                license_number: "",
                years_of_experience: 0,
                status: "AVAILABLE",
                rating: 5,
            });

        }

    }, [open, mode, driver]);

    if (!open) return null;

    function change(
        e: React.ChangeEvent<
            HTMLInputElement | HTMLSelectElement
        >
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
                    width: "700px",
                    maxWidth: "95%",
                    background: "#fff",
                    boxShadow: "0 15px 40px rgba(0,0,0,.25)",
                    borderRadius: 12,
                    padding: "32px 36px",
                    maxHeight: "90vh",
                    overflowY: "auto",
                    scrollbarWidth: "thin",
                }}
            >

                <h2
                    style={{
                        textAlign: "center",
                        color: "#1e293b",
                    }}
                >
                    {mode === "add"
                        ? "✏️ Edit Driver"
                        : "✏️ Edit Driver"}
                </h2>

                <p
                    style={{
                        textAlign: "center",
                        color: "#6b7280",
                        marginBottom: 25,
                    }}
                >
                    {mode === "add"
                        ? "Fill all driver information."
                        : `Employee ID: ${form.employee_id}`}
                </p>

                <label style={label}>
                    Employee ID
                </label>

                <input
                    name="employee_id"
                    value={form.employee_id || ""}
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

                <label style={label}>
                    First Name
                </label>

                <input
                    name="first_name"
                    value={form.first_name || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Last Name
                </label>

                <input
                    name="last_name"
                    value={form.last_name || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Email
                </label>

                <input
                    name="email"
                    type="email"
                    value={form.email || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    Phone
                </label>

                <input
                    type="tel"
                    name="phone"
                    value={form.phone || ""}
                    onChange={change}
                    style={input}
                />

                <label style={label}>
                    License Number
                </label>

                <input
                    name="license_number"
                    value={form.license_number || ""}
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

                <label style={label}>
                    Experience (Years)
                </label>

                <input
                    type="number"
                    name="years_of_experience"
                    value={
                        form.years_of_experience || 0
                    }
                    onChange={change}
                    style={input}
                />

                {mode === "edit" && (
                    <>
                        <label style={label}>
                            Status
                        </label>

                        <select
                            name="status"
                            value={form.status || ""}
                            onChange={change}
                            style={input}
                        >
                            <option value="AVAILABLE">🟢 AVAILABLE</option>

                            <option value="ON_DELIVERY">🚚 ON DELIVERY</option>

                            <option value="OFFLINE">⚫ OFFLINE</option>

                            <option value="ON_BREAK">☕ ON BREAK</option>

                            <option value="LEAVE">🌴 LEAVE</option>
                        </select>

                        <label style={label}>
                            Rating
                        </label>

                        <input
                            type="number"
                            step="0.1"
                            min="0"
                            max="5"
                            name="rating"
                            value={form.rating || 0}
                            onChange={change}
                            style={input}
                        />
                    </>
                )}

                <div
                    style={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "center",
                        marginTop: 30,
                    }}
                >

                    <button
                        onClick={onClose}
                        style={cancelBtn}
                    >
                        ✖ Cancel
                    </button>

                    <button
                        onClick={() =>
                            onSave(form)
                        }
                        style={saveBtn}
                    >
                        {mode === "add"
                            ? "➕ Create Driver"
                            : "💾 Save Changes"}
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
    outline:"none",
    transform:"translateY(0)",
    transition:"all .25s ease",
    padding:"13px 14px",
    borderRadius: 8,
    border:"1px solid #e5e7eb",
    fontSize: 15,
    boxSizing: "border-box" as const,
};

const cancelBtn = {
    padding: "10px 20px",
    border: "none",
    borderRadius: 8,
    background: "#6b7280",
    color: "white",
    cursor: "pointer",
};

const saveBtn = {
    padding: "10px 22px",
    border: "none",
    borderRadius: 8,
    background: "#2563eb",
    color: "white",
    cursor: "pointer",
    fontWeight: 600,
};