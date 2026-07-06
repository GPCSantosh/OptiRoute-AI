type Props = {
    result: any;
};

export default function RoutePathTable({
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
                background: "#ffffff",
                borderRadius: 14,
                padding: 24,
                marginTop: 25,
                boxShadow: "0 8px 22px rgba(0,0,0,.08)",
            }}
        >

            <h2
                style={{
                    marginTop: 0,
                    color: "#1e293b",
                    marginBottom: 20,
                }}
            >
                🛣 Route Path
            </h2>

            <table
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                }}
            >

                <thead>

                    <tr
                        style={{
                            background: "#1e293b",
                            color: "white",
                        }}
                    >

                        <th style={th}>
                            Step
                        </th>

                        <th style={th}>
                            City
                        </th>

                        <th style={th}>
                            Type
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {result.path.map(
                        (
                            city: string,
                            index: number
                        ) => (

                            <tr
                                key={index}
                                style={{
                                    borderBottom:
                                        "1px solid #e5e7eb",
                                }}
                            >

                                <td style={td}>
                                    {index + 1}
                                </td>

                                <td style={td}>
                                    {city}
                                </td>

                                <td style={td}>

                                    {index === 0 ? (

                                        <span
                                            style={startBadge}
                                        >
                                            Source
                                        </span>

                                    ) : index ===
                                      result.path.length -
                                          1 ? (

                                        <span
                                            style={endBadge}
                                        >
                                            Destination
                                        </span>

                                    ) : (

                                        <span
                                            style={middleBadge}
                                        >
                                            Intermediate
                                        </span>

                                    )}

                                </td>

                            </tr>

                        )

                    )}

                </tbody>

            </table>

        </div>

    );

}

const th = {
    padding: "14px",
    textAlign: "left" as const,
};

const td = {
    padding: "14px",
};

const startBadge = {
    background: "#dcfce7",
    color: "#166534",
    padding: "6px 14px",
    borderRadius: 20,
    fontWeight: 600,
};

const middleBadge = {
    background: "#dbeafe",
    color: "#1d4ed8",
    padding: "6px 14px",
    borderRadius: 20,
    fontWeight: 600,
};

const endBadge = {
    background: "#fee2e2",
    color: "#b91c1c",
    padding: "6px 14px",
    borderRadius: 20,
    fontWeight: 600,
};