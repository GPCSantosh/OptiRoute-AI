import DashboardLayout from "../layouts/DashboardLayout";

import VehicleToolbar from "../components/vehicles/VehicleToolbar";
import VehicleTable from "../components/vehicles/VehicleTable";

export default function Vehicles() {

    return (

        <DashboardLayout>

            <VehicleToolbar />

            <VehicleTable />

        </DashboardLayout>

    );

}