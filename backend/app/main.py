from contextlib import asynccontextmanager
from app.roads.router import router as roads_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from app.drivers.router import router as driver_router
from app.api.v1.health import router as health_router
from app.auth.router import router as auth_router
from app.core.config import settings
from app.core.logger import logger
from app.db.base import Base
from app.db.session import engine
from app.middleware.request_id import RequestIDMiddleware
from app.orders.router import router as order_router
from app.users.router import router as user_router
from app.vehicles.router import router as vehicle_router
from app.warehouses.router import router as warehouse_router
import asyncio

from app.simulation.vehicle_simulator import vehicle_simulator
from app.simulation.traffic_simulator import traffic_simulator

from app.api.v1.analytics import router as analytics_router
from app.api.v1.routes import router as routes_router
from app.api.v1.simulation import router as simulation_router
from app.api.v1.traffic import router as traffic_router
from sqlalchemy.ext.asyncio import AsyncEngine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown.
    """

    @asynccontextmanager
    async def lifespan(app: FastAPI):

        logger.info("Creating database tables...")

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        logger.info("Database tables created.")

    # existing simulator code...
    logger.info("=" * 60)
    logger.info(f"Starting {settings.APP_NAME}")
    logger.info(f"Version : {settings.APP_VERSION}")
    logger.info(
        f"Environment : {'Development' if settings.DEBUG else 'Production'}"
    )
    logger.info("=" * 60)

    # Future startup tasks:
    # await create_db()
    # await create_admin()
    # await redis_connect()
    vehicle_simulator.add_vehicle(
    1,
    17.728,
    83.304,
    )

    vehicle_simulator.add_vehicle(
        2,
        17.730,
        83.310,
    )

    traffic_simulator.add_road(1)
    traffic_simulator.add_road(2)
    traffic_simulator.add_road(3)

    vehicle_task = asyncio.create_task(
        vehicle_simulator.run()
    )

    traffic_task = asyncio.create_task(
        traffic_simulator.run()
    )

    yield

    logger.info("=" * 60)
    logger.info("Stopping OptiRoute AI Backend")
    logger.info("=" * 60)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Production-grade Intelligent Route Optimization & Fleet Management Platform",
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

# --------------------------------------------------------
# Middleware
# --------------------------------------------------------

app.add_middleware(RequestIDMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------------
# Health
# --------------------------------------------------------

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)

# --------------------------------------------------------
# Authentication
# --------------------------------------------------------

app.include_router(
    auth_router,
    prefix=settings.API_V1_PREFIX,
)

# --------------------------------------------------------
# Users
# --------------------------------------------------------

app.include_router(
    user_router,
    prefix=settings.API_V1_PREFIX,
)

# --------------------------------------------------------
# Vehicles
# --------------------------------------------------------

app.include_router(
    vehicle_router,
    prefix=settings.API_V1_PREFIX,
)

# --------------------------------------------------------
# Drivers
# --------------------------------------------------------

app.include_router(
    driver_router,
    prefix=settings.API_V1_PREFIX,
)

# --------------------------------------------------------
# Warehouses
# --------------------------------------------------------

app.include_router(
    warehouse_router,
    prefix=settings.API_V1_PREFIX,
)

# --------------------------------------------------------
# Orders
# --------------------------------------------------------

app.include_router(
    order_router,
    prefix=settings.API_V1_PREFIX,
)

from app.websocket.routes import router as websocket_router

app.include_router(
    websocket_router,
)

from app.tracking.router import router as tracking_router
app.include_router(
    tracking_router,
    prefix=settings.API_V1_PREFIX,
)

from app.routes.router import router as route_router

app.include_router(
    route_router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    analytics_router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    routes_router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    simulation_router,
    prefix=settings.API_V1_PREFIX,
)

app.include_router(
    traffic_router,
    prefix=settings.API_V1_PREFIX,
)
app.include_router(
    roads_router,
    prefix=settings.API_V1_PREFIX,
)

# --------------------------------------------------------
# Root
# --------------------------------------------------------

@app.get("/", tags=["Root"])
async def root():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running",
        "docs": "/docs",
        "redoc": "/redoc",
    }