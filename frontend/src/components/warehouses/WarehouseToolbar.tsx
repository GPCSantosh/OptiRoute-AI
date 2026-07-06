type Props = {
    search: string;
    setSearch: (value: string) => void;
    onAdd: () => void;
};

export default function WarehouseToolbar({
    search,
    setSearch,
    onAdd,
}: Props) {
    return (
        <>
            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginBottom: 25,
                }}
            >
                <div>
                    <h1
                        style={{
                            margin: 0,
                            color: "#0f172a",
                            fontSize: 36,
                            fontWeight: 700,
                        }}
                    >
                        Warehouses
                    </h1>

                    <p
                        style={{
                            marginTop: 8,
                            color: "#64748b",
                            fontSize: 15,
                        }}
                    >
                        Manage warehouse locations and storage capacity
                    </p>
                </div>

                <button
                    onClick={onAdd}
                    style={{
                        background: "#2563eb",
                        color: "#fff",
                        border: "none",
                        padding: "13px 22px",
                        borderRadius: 10,
                        cursor: "pointer",
                        fontWeight: 600,
                        fontSize: 15,
                        boxShadow: "0 8px 18px rgba(37,99,235,.25)",
                    }}
                >
                    + Add Warehouse
                </button>
            </div>

            <input
                type="text"
                placeholder="Search by Warehouse Code, Name, City or State..."
                value={search}
                onChange={(e) =>
                    setSearch(e.target.value)
                }
                style={{
                    width: "100%",
                    padding: "14px 16px",
                    marginBottom: 28,
                    borderRadius: 10,
                    border: "1px solid #cbd5e1",
                    fontSize: 15,
                    outline: "none",
                    boxSizing: "border-box",
                }}
            />
        </>
    );
}