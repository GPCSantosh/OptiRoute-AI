import { useQuery } from "@tanstack/react-query";
import { getWarehouses } from "../api/warehouses";

export function useWarehouses() {
    return useQuery({
        queryKey: ["warehouses"],
        queryFn: getWarehouses,
    });
}