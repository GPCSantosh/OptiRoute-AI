type Props = {
    warehouses: any[];
    source: string;
    destination: string;
    algorithm: string;

    onSourceChange: (value: string) => void;
    onDestinationChange: (value: string) => void;
    onAlgorithmChange: (value: string) => void;

    onOptimize: () => void;

    loading: boolean;
};

export default function RouteOptimizerToolbar({

    warehouses,

    source,

    destination,

    algorithm,

    onSourceChange,

    onDestinationChange,

    onAlgorithmChange,

    onOptimize,

    loading,

}: Props) {

    const uniqueCities = Array.from(
        new Set(
            warehouses.map(
                (warehouse: any) => warehouse.city
            )
        )
    );
    return (

        <div
            style={{
                background: "white",
                borderRadius: 14,
                padding: 24,
                marginBottom: 30,
                boxShadow: "0 10px 25px rgba(0,0,0,.08)",
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    color: "#1e293b",
                    marginBottom: 20,
                }}
            >
                🚚 Route Optimizer
            </h2>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns:
                        "repeat(auto-fit,minmax(240px,1fr))",
                    gap: 18,
                }}
            >

                <div>

                    <label style={label}>
                        Source Warehouse
                    </label>

                    <select
                        value={source}
                        onChange={(e) =>
                            onSourceChange(
                                e.target.value
                            )
                        }
                        style={input}
                    >

                        <option value="">
                            Select Source
                        </option>

                        {uniqueCities.map((city: string) => (

                            <option
                                key={city}
                                value={city}
                            >
                                {city}
                            </option>

                        ))}

                    </select>

                </div>

                <div>

                    <label style={label}>
                        Destination Warehouse
                    </label>

                    <select
                        value={destination}
                        onChange={(e) =>
                            onDestinationChange(
                                e.target.value
                            )
                        }
                        style={input}
                    >

                        <option value="">
                            Select Destination
                        </option>

                        {uniqueCities.map((city: string) => (

                            <option
                                key={city}
                                value={city}
                            >
                                {city}
                            </option>

                        ))}

                    </select>

                </div>

                <div>

                    <label style={label}>
                        Algorithm
                    </label>

                    <select
                        value={algorithm}
                        onChange={(e) =>
                            onAlgorithmChange(
                                e.target.value
                            )
                        }
                        style={input}
                    >

                        <option value="dijkstra">
                            Dijkstra
                        </option>

                        <option value="astar">
                            A*
                        </option>

                    </select>

                </div>

            </div>

            <div
                style={{
                    marginTop: 25,
                    display: "flex",
                    justifyContent: "flex-end",
                }}
            >

                <button
                    disabled={
                        loading ||
                        !source ||
                        !destination
                    }
                    onClick={onOptimize}
                    style={{
                        background:
                            loading
                                ? "#94a3b8"
                                : "#2563eb",
                        color: "white",
                        border: "none",
                        padding:
                            "12px 26px",
                        borderRadius: 8,
                        cursor: loading
                            ? "not-allowed"
                            : "pointer",
                        fontWeight: 600,
                        fontSize: 15,
                    }}
                >
                    {loading
                        ? "Optimizing..."
                        : "🚀 Optimize Route"}
                </button>

            </div>

        </div>

    );

}

const label = {

    display: "block",

    marginBottom: 8,

    fontWeight: 600,

    color: "#334155",

};

const input = {

    width: "100%",

    padding: 12,

    borderRadius: 8,

    border: "1px solid #d1d5db",

    fontSize: 15,

    boxSizing: "border-box" as const,

};