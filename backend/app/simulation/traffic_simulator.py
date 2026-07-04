from __future__ import annotations

import asyncio
import random

from app.websocket.manager import manager


class TrafficSimulator:

    def __init__(self):

        self.roads = {}

        self.running = False

    def add_road(
        self,
        road_id: int,
    ):

        self.roads[road_id] = {
            "road_id": road_id,
            "traffic_level": random.randint(0, 30),
            "speed_limit": 60,
            "closed": False,
            "weather": "CLEAR",
        }

    async def update_road(self, road):

        road["traffic_level"] = random.randint(
            0,
            100,
        )

        if road["traffic_level"] > 90:

            road["closed"] = True

        else:

            road["closed"] = False

        await manager.broadcast(
            {
                "type": "traffic",
                "payload": road,
            }
        )

    async def run(self):

        self.running = True

        while self.running:

            for road in self.roads.values():

                await self.update_road(road)

            await asyncio.sleep(5)

    def stop(self):

        self.running = False


traffic_simulator = TrafficSimulator()