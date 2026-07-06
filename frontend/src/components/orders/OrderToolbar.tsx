import { useState } from "react";

type Props = {
    onAdd: () => void;
    onSearch?: (value: string) => void;
};

export default function OrderToolbar({
    onAdd,
    onSearch,
}: Props) {
    const [search, setSearch] = useState("");

    function handleSearch(
        e: React.ChangeEvent<HTMLInputElement>
    ) {
        const value = e.target.value;

        setSearch(value);

        onSearch?.(value);
    }

    return (
        <div
            style={{
                width: "100%",
                marginBottom: 25,
            }}
        >
            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    marginBottom: 20,
                }}
            >
                <div>
                    <h1
                        style={{
                            margin: 0,
                            fontSize: 30,
                            color: "#1e293b",
                            fontWeight: 700,
                        }}
                    >
                        Orders
                    </h1>

                    <p
                        style={{
                            marginTop: 6,
                            color: "#64748b",
                            fontSize: 15,
                        }}
                    >
                        Manage customer delivery orders
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
                        fontWeight: 600,
                        fontSize: 15,
                    }}
                >
                    + Add Order
                </button>
            </div>

            <div
                style={{
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    gap: 20,
                }}
            >
                <input
                    type="text"
                    placeholder="Search by Order Number, Customer or Phone..."
                    value={search}
                    onChange={handleSearch}
                    style={{
                        width: "100%",
                        maxWidth: 420,
                        padding: "12px 16px",
                        borderRadius: 10,
                        border: "1px solid #d1d5db",
                        outline: "none",
                        fontSize: 15,
                    }}
                />
            </div>
        </div>
    );
}