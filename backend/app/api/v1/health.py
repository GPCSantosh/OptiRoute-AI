from datetime import datetime, timezone

from fastapi import APIRouter, status

from app.core.config import settings
from app.db.session import check_database_connection

router = APIRouter(prefix="/health", tags=["Health"])

# Application startup time
START_TIME = datetime.now(timezone.utc)


@router.api_route(
    "/",
    methods=["GET", "HEAD"],
    status_code=status.HTTP_200_OK,
)
async def health_check():
    """
    Returns application health information.
    """

    db_connected = await check_database_connection()

    return {
        "status": "healthy" if db_connected else "unhealthy",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "database": "connected" if db_connected else "disconnected",
        "server_time": datetime.now(timezone.utc).isoformat(),
        "started_at": START_TIME.isoformat(),
    }


@router.api_route(
    "/live",
    methods=["GET", "HEAD"],
)
async def liveness():
    """
    Kubernetes Liveness Probe.

    Returns 200 if application is alive.
    """

    return {
        "alive": True
    }

@router.api_route(
    "/ready",
    methods=["GET", "HEAD"],
)
async def readiness():
    """
    Kubernetes Readiness Probe.

    Returns 200 only when dependencies are available.
    """

    database = await check_database_connection()

    if database:

        return {
            "ready": True
        }

    return {
        "ready": False
    }