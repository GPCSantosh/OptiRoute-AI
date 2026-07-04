export interface Vehicle {
    id: number;
    registration_number: string;
    vehicle_name: string;
    manufacturer: string;
    model: string;
    capacity_kg: number;
    fuel_capacity: number;
    current_fuel: number;
    mileage: number;
    max_speed: number;
    fuel_type: string;
    status?: string;
    is_available?: boolean;
}