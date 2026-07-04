from __future__ import annotations

import json
from collections import defaultdict

from fastapi import WebSocket


class ConnectionManager:
    """
    Manages active websocket connections.

    Supports:
    - Global broadcasts
    - Vehicle-specific channels
    - Order-specific channels
    """

    def __init__(self):

        self.active_connections: list[WebSocket] = []

        self.vehicle_rooms = defaultdict(list)

        self.order_rooms = defaultdict(list)

    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):

        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

        for room in self.vehicle_rooms.values():
            if websocket in room:
                room.remove(websocket)

        for room in self.order_rooms.values():
            if websocket in room:
                room.remove(websocket)

    async def broadcast(
        self,
        message: dict,
    ):

        dead = []

        payload = json.dumps(message)

        for connection in self.active_connections:

            try:
                await connection.send_text(payload)

            except Exception:
                dead.append(connection)

        for connection in dead:
            self.disconnect(connection)

    async def send_vehicle_update(
        self,
        vehicle_id: int,
        data: dict,
    ):

        payload = json.dumps(data)

        dead = []

        for websocket in self.vehicle_rooms[vehicle_id]:

            try:
                await websocket.send_text(payload)

            except Exception:
                dead.append(websocket)

        for websocket in dead:
            self.disconnect(websocket)

    async def send_order_update(
        self,
        order_id: int,
        data: dict,
    ):

        payload = json.dumps(data)

        dead = []

        for websocket in self.order_rooms[order_id]:

            try:
                await websocket.send_text(payload)

            except Exception:
                dead.append(websocket)

        for websocket in dead:
            self.disconnect(websocket)

    async def join_vehicle(
        self,
        websocket: WebSocket,
        vehicle_id: int,
    ):

        if websocket not in self.vehicle_rooms[vehicle_id]:
            self.vehicle_rooms[vehicle_id].append(websocket)

    async def join_order(
        self,
        websocket: WebSocket,
        order_id: int,
    ):

        if websocket not in self.order_rooms[order_id]:
            self.order_rooms[order_id].append(websocket)


manager = ConnectionManager()