from __future__ import annotations

from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.manager import manager

router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"],
)


@router.websocket("/")
async def websocket_root(
    websocket: WebSocket,
):

    await manager.connect(websocket)

    try:

        while True:

            message = await websocket.receive_text()

            await manager.broadcast(
                {
                    "type": "message",
                    "payload": message,
                }
            )

    except WebSocketDisconnect:

        manager.disconnect(websocket)


@router.websocket("/vehicles/{vehicle_id}")
async def websocket_vehicle(
    websocket: WebSocket,
    vehicle_id: int,
):

    await manager.connect(websocket)

    await manager.join_vehicle(
        websocket,
        vehicle_id,
    )

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        manager.disconnect(websocket)


@router.websocket("/orders/{order_id}")
async def websocket_order(
    websocket: WebSocket,
    order_id: int,
):

    await manager.connect(websocket)

    await manager.join_order(
        websocket,
        order_id,
    )

    try:

        while True:

            await websocket.receive_text()

    except WebSocketDisconnect:

        manager.disconnect(websocket)