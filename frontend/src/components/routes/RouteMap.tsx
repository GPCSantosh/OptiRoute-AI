type Props = {
    result: any;
};

export default function RouteMap({
    result,
}: Props) {

    if (
        !result ||
        !result.path ||
        result.path.length === 0
    ) {
        return null;
    }

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
                    marginBottom: 20,
                    color: "#1e293b",
                }}
            >
                🗺 Route Visualization
            </h2>

            <div
                style={{
                    minHeight: 260,
                    borderRadius: 12,
                    background:
                        "linear-gradient(135deg,#eff6ff,#f8fafc)",
                    border: "2px dashed #93c5fd",
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "center",
                    alignItems: "center",
                    padding: 25,
                }}
            >

                <div
                    style={{
                        fontSize: 55,
                    }}
                >
                    🗺️
                </div>

                <h3
                    style={{
                        marginBottom: 10,
                        color: "#1e293b",
                    }}
                >
                    Optimized Route
                </h3>

                <div
                    style={{
                        display: "flex",
                        flexWrap: "wrap",
                        justifyContent: "center",
                        gap: 8,
                        fontSize: 16,
                        fontWeight: 600,
                        color: "#334155",
                    }}
                >

                    {result.path.map(
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
                                                "0 10px",
                                            fontWeight: 700,
                                        }}
                                    >
                                        →
                                    </span>

                                )}

                            </span>

                        )
                    )}

                </div>

                <div
                    style={{
                        marginTop: 25,
                        color: "#64748b",
                        textAlign: "center",
                        lineHeight: 1.7,
                    }}
                >
                    Interactive OpenStreetMap / Leaflet
                    visualization will be integrated in
                    the next phase.
                </div>

            </div>

        </div>

    );

}