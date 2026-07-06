type Props = {
    result: any;
};

export default function RouteStatistics({
    result,
}: Props) {

    if (
        !result ||
        !result.path ||
        result.path.length === 0
    ) {
        return null;
    }

    const distance =
        Number(result.distance ?? 0);

    const execution =
        Number(result.execution_time_ms ?? 0);

    const visited =
        Number(result.visited_nodes ?? 0);

    const expanded =
        Number(result.expanded_nodes ?? 0);

    const travelTime =
        Number(result.travel_time ?? 0);

    const averageSpeed =
        travelTime > 0
            ? (
                  distance /
                  (travelTime / 60)
              ).toFixed(2)
            : "--";

    return (

        <div
            style={{
                marginTop: 25,
                background: "white",
                borderRadius: 14,
                padding: 24,
                boxShadow:
                    "0 10px 24px rgba(0,0,0,.08)",
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    marginBottom: 22,
                    color: "#1e293b",
                }}
            >
                📈 Route Statistics
            </h2>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns:
                        "repeat(auto-fit,minmax(200px,1fr))",
                    gap: 18,
                }}
            >

                <StatCard
                    title="Distance"
                    value={`${distance} km`}
                    color="#2563eb"
                />

                <StatCard
                    title="Execution Time"
                    value={`${execution} ms`}
                    color="#9333ea"
                />

                <StatCard
                    title="Visited Nodes"
                    value={visited}
                    color="#16a34a"
                />

                <StatCard
                    title="Expanded Nodes"
                    value={expanded}
                    color="#ea580c"
                />

                <StatCard
                    title="Travel Time"
                    value={
                        travelTime > 0
                            ? `${travelTime} min`
                            : "--"
                    }
                    color="#0891b2"
                />

                <StatCard
                    title="Average Speed"
                    value={
                        averageSpeed === "--"
                            ? "--"
                            : `${averageSpeed} km/h`
                    }
                    color="#dc2626"
                />

            </div>

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
                borderRadius: 12,
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
                    fontSize: 26,
                    fontWeight: 700,
                    color: "#0f172a",
                }}
            >
                {value}
            </div>

        </div>

    );

}