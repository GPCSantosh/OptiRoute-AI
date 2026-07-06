type Props = {
    onAdd: () => void;
};

export default function VehicleToolbar({
    onAdd,
}: Props) {

    return (

        <div
            style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: 20,
            }}
        >

            <h2
                style={{
                    margin: 0,
                    color: "#1e293b",
                }}
            >
                Vehicles
            </h2>

            <button
                onClick={onAdd}
                style={{
                    background: "#2563eb",
                    color: "white",
                    border: "none",
                    padding: "10px 18px",
                    borderRadius: 8,
                    cursor: "pointer",
                    fontWeight: 600,
                }}
            >
                + Add Vehicle
            </button>

        </div>

    );

}