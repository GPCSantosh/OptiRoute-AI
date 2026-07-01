from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from app.core.config import settings
from app.core.logger import logger


# Routers
from app.api.v1.health import router as health_router

# Database
from app.db.session import engine

# Base metadata (imports all models later)
from app.db.base import Base

from app.auth.router import router as auth_router
app.include_router(
    auth_router,
    prefix=settings.API_V1_PREFIX,
)
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and Shutdown Events
    """

    logger.info("========================================")
    logger.info("Starting OptiRoute AI Backend...")
    logger.info(f"Environment : {'Development' if settings.DEBUG else 'Production'}")
    logger.info(f"Version     : {settings.APP_VERSION}")
    logger.info("========================================")

    yield

    logger.info("Stopping OptiRoute AI Backend...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Intelligent Route Optimization & Fleet Management Platform",
    default_response_class=ORJSONResponse,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)
from app.middleware.request_id import RequestIDMiddleware
app.add_middleware(RequestIDMiddleware)

# --------------------------------------------------------
# CORS
# --------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------------
# API Routers
# --------------------------------------------------------

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)


# --------------------------------------------------------
# Root Endpoint
# --------------------------------------------------------

@app.get("/", tags=["Root"])
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "Running",
        "docs": "/docs",
    }

from app.users.router import (
    router as user_router,
)

app.include_router(
    user_router,
    prefix=settings.API_V1_PREFIX,
)


from app.vehicles.router import (
    router as vehicle_router,
)

app.include_router(
    vehicle_router,
    prefix=settings.API_V1_PREFIX,
)


from app.warehouses.router import (
    router as warehouse_router,
)

app.include_router(
    warehouse_router,
    prefix=settings.API_V1_PREFIX,
)

from app.orders.router import router as order_router

app.include_router(
    order_router,
    prefix=settings.API_V1_PREFIX,
)