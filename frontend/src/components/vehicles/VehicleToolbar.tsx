export default function VehicleToolbar() {

    return (

        <div className="flex justify-between items-center mb-6">

            <h1 className="text-3xl font-bold">

                Vehicles

            </h1>

            <button
                className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700"
            >

                + Add Vehicle

            </button>

        </div>

    );

}