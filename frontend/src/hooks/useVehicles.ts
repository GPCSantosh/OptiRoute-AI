import { useQuery } from "@tanstack/react-query";
import { getVehicles } from "../api/vehicles";

export function useVehicles() {
    return useQuery({
        queryKey: ["vehicles"],
        queryFn: getVehicles,
    });
}