type Props = {
    onAdd: () => void;
};

export default function DriverToolbar({
    onAdd,
}: Props) {
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                width: "100%",
                marginBottom: 24,
                padding: "0 4px",
            }}
        >
            <div>
                <h1
                    style={{
                        margin: 0,
                        fontSize: 30,
                        fontWeight: 700,
                        color: "#1e293b",
                    }}
                >
                    Drivers
                </h1>

                <p
                    style={{
                        margin: "6px 0 0",
                        color: "#64748b",
                        fontSize: 15,
                    }}
                >
                    Manage all drivers in your fleet
                </p>
            </div>

            <button
                onClick={onAdd}
                style={{
                    background: "#2563eb",
                    color: "#fff",
                    border: "none",
                    borderRadius: 10,
                    padding: "12px 22px",
                    cursor: "pointer",
                    fontWeight: 700,
                    fontSize: 15,
                    boxShadow: "0 4px 12px rgba(37,99,235,.25)",
                    transition: "0.2s",
                }}
                onMouseEnter={(e) => {
                    e.currentTarget.style.background = "#1d4ed8";
                }}
                onMouseLeave={(e) => {
                    e.currentTarget.style.background = "#2563eb";
                }}
            >
                + Add Driver
            </button>
        </div>
    );
}