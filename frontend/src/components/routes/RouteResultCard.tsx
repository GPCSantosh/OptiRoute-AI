type Props = {
    result: any;
};

export default function RouteResultCard({
    result,
}: Props) {

    if (!result) return null;

    return (

        <div
            style={{
                background: "white",
                borderRadius: 14,
                padding: 24,
                marginBottom: 25,
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
                📊 Optimization Result
            </h2>

            {(!result.path || result.path.length === 0) && (

                <div
                    style={{
                        background: "#fee2e2",
                        color: "#991b1b",
                        padding: 18,
                        borderRadius: 10,
                        fontWeight: 600,
                    }}
                >
                    ❌ {result.message || "No route found."}
                </div>

            )}

            {result.path && result.path.length > 0 && (

                <>

                    <div
                        style={{
                            display: "grid",
                            gridTemplateColumns:
                                "repeat(auto-fit,minmax(220px,1fr))",
                            gap: 18,
                        }}
                    >

                        <StatCard
                            title="Algorithm"
                            value={result.algorithm}
                            color="#2563eb"
                        />

                        <StatCard
                            title="Distance"
                            value={`${result.distance} km`}
                            color="#16a34a"
                        />

                        <StatCard
                            title="Execution Time"
                            value={`${result.execution_time_ms} ms`}
                            color="#9333ea"
                        />

                        <StatCard
                            title="Visited Nodes"
                            value={result.visited_nodes}
                            color="#ea580c"
                        />

                        <StatCard
                            title="Expanded Nodes"
                            value={result.expanded_nodes}
                            color="#0891b2"
                        />

                    </div>

                    <div
                        style={{
                            marginTop: 30,
                            background: "#f8fafc",
                            borderRadius: 10,
                            padding: 18,
                        }}
                    >

                        <h3
                            style={{
                                marginTop: 0,
                                color: "#0f172a",
                            }}
                        >
                            🛣 Optimized Route
                        </h3>

                        <div
                            style={{
                                display: "flex",
                                flexWrap: "wrap",
                                alignItems: "center",
                                gap: 8,
                                fontSize: 16,
                                fontWeight: 600,
                                color: "#334155",
                            }}
                        >

                            {result.path?.map(
                                (
                                    city: string,
                                    index: number
                                ) => (

                                    <span
                                        key={index}
                                    >

                                        {city}

                                        {index <
                                            result.path.length - 1 && (
                                            <span
                                                style={{
                                                    color: "#2563eb",
                                                    margin:
                                                        "0 8px",
                                                }}
                                            >
                                                →
                                            </span>
                                        )}

                                    </span>

                                )
                            )}

                        </div>

                    </div>

                </>

            )}

        </div>

    );

}

function StatCard({
    title,
    value,
    color,
}: {
    title: string;
    value: any;
    color: string;
}) {

    return (

        <div
            style={{
                background: "#f8fafc",
                borderRadius: 10,
                padding: 18,
                borderLeft: `6px solid ${color}`,
            }}
        >

            <div
                style={{
                    color: "#64748b",
                    fontSize: 14,
                }}
            >
                {title}
            </div>

            <div
                style={{
                    marginTop: 10,
                    fontSize: 24,
                    fontWeight: 700,
                    color: "#0f172a",
                }}
            >
                {value}
            </div>

        </div>

    );

}