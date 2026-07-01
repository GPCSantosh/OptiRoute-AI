import os
import sys
from pathlib import Path

from loguru import logger

from app.core.config import settings

# --------------------------------------------------------------------
# Create logs directory automatically
# --------------------------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------------------------
# Remove default logger
# --------------------------------------------------------------------

logger.remove()

# --------------------------------------------------------------------
# Console Logger
# --------------------------------------------------------------------

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    colorize=True,
    enqueue=True,
    backtrace=True,
    diagnose=settings.DEBUG,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    ),
)

# --------------------------------------------------------------------
# General Application Log
# --------------------------------------------------------------------

logger.add(
    LOG_DIR / "backend.log",
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=settings.DEBUG,
)

# --------------------------------------------------------------------
# Error Log
# --------------------------------------------------------------------

logger.add(
    LOG_DIR / "errors.log",
    level="ERROR",
    rotation="5 MB",
    retention="60 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

# --------------------------------------------------------------------
# Database Log
# --------------------------------------------------------------------

logger.add(
    LOG_DIR / "database.log",
    level="DEBUG",
    rotation="10 MB",
    retention="30 days",
    filter=lambda record: record["extra"].get("module") == "database",
)

# --------------------------------------------------------------------
# Algorithm Log
# --------------------------------------------------------------------

logger.add(
    LOG_DIR / "algorithms.log",
    level="DEBUG",
    rotation="10 MB",
    retention="30 days",
    filter=lambda record: record["extra"].get("module") == "algorithm",
)

# --------------------------------------------------------------------
# API Log
# --------------------------------------------------------------------

logger.add(
    LOG_DIR / "api.log",
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    filter=lambda record: record["extra"].get("module") == "api",
)