import { useVehicles } from "./useVehicles";
import { useOrders } from "./useOrders";
import { useWarehouses } from "./useWarehouses";

export function useDashboard() {

    const vehicles = useVehicles();

    const orders = useOrders();

    const warehouses = useWarehouses();

    return {

        vehicles,

        orders,

        warehouses,

        loading:
            vehicles.isLoading ||
            orders.isLoading ||
            warehouses.isLoading,

    };
}