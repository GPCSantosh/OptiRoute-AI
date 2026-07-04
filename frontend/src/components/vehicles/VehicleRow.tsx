interface Props {
    vehicle: any;
}

export default function VehicleRow({ vehicle }: Props) {
    return (
        <tr className="border-b hover:bg-gray-50">
            <td className="p-4">{vehicle.vehicle_name}</td>
            <td>{vehicle.registration_number}</td>
            <td>{vehicle.capacity_kg} kg</td>
            <td>{vehicle.current_fuel} L</td>
            <td>{vehicle.status ?? "AVAILABLE"}</td>
            <td>
                <button className="text-blue-600 mr-3">
                    Edit
                </button>

                <button className="text-red-600">
                    Delete
                </button>
            </td>
        </tr>
    );
}