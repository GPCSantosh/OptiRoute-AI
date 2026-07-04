from __future__ import annotations

import asyncio
import random

from app.websocket.manager import manager


class VehicleSimulator:
    """
    Simulates vehicle movement.

    Future upgrades:
    - Dijkstra routing
    - Traffic delays
    - Fuel prediction
    - ETA prediction
    - GPS tracking
    """

    def __init__(self):

        self.vehicles: dict[int, dict] = {}

        self.running = False

    def add_vehicle(
        self,
        vehicle_id: int,
        latitude: float,
        longitude: float,
    ):

        self.vehicles[vehicle_id] = {
            "vehicle_id": vehicle_id,
            "latitude": latitude,
            "longitude": longitude,
            "speed": random.randint(30, 70),
            "fuel": 100.0,
            "status": "MOVING",
            "eta": random.randint(20, 120),
        }

    def remove_vehicle(
        self,
        vehicle_id: int,
    ):

        self.vehicles.pop(vehicle_id, None)

    async def update_vehicle(
        self,
        vehicle: dict,
    ):

        vehicle["latitude"] += random.uniform(
            -0.0008,
            0.0008,
        )

        vehicle["longitude"] += random.uniform(
            -0.0008,
            0.0008,
        )

        vehicle["fuel"] = max(
            vehicle["fuel"] - random.uniform(0.02, 0.10),
            0,
        )

        vehicle["eta"] = max(
            vehicle["eta"] - 1,
            0,
        )

        await manager.send_vehicle_update(
            vehicle["vehicle_id"],
            vehicle,
        )

    async def run(self):

        self.running = True

        while self.running:

            for vehicle in list(self.vehicles.values()):

                await self.update_vehicle(
                    vehicle
                )

            await asyncio.sleep(1)

    def stop(self):

        self.running = False


vehicle_simulator = VehicleSimulator()