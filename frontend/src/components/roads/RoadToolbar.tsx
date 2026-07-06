import type { ChangeEvent } from "react";

type Props = {
    search: string;
    onSearch: (value: string) => void;
    onAdd: () => void;
};

export default function RoadToolbar({
    search,
    onSearch,
    onAdd,
}: Props) {
    function handleSearch(
        e: ChangeEvent<HTMLInputElement>
    ) {
        onSearch(e.target.value);
    }

    return (
        <>
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
                            color: "#0f172a",
                            fontSize: 42,
                            fontWeight: 700,
                        }}
                    >
                        Roads
                    </h1>

                    <p
                        style={{
                            marginTop: 8,
                            color: "#64748b",
                            fontSize: 16,
                        }}
                    >
                        Manage road network and traffic information
                    </p>
                </div>

                <button
                    onClick={onAdd}
                    style={{
                        background: "#2563eb",
                        color: "#fff",
                        border: "none",
                        padding: "14px 24px",
                        borderRadius: 10,
                        cursor: "pointer",
                        fontWeight: 600,
                        fontSize: 15,
                        boxShadow:
                            "0 8px 18px rgba(37,99,235,.25)",
                    }}
                >
                    + Add Road
                </button>
            </div>

            <input
                type="text"
                value={search}
                onChange={handleSearch}
                placeholder="Search by Road Name, Source or Destination..."
                style={{
                    width: "100%",
                    maxWidth: 600,
                    marginBottom: 24,
                    padding: "14px 16px",
                    borderRadius: 10,
                    border: "1px solid #d1d5db",
                    outline: "none",
                    fontSize: 15,
                    transition: ".25s",
                }}
            />
        </>
    );
}