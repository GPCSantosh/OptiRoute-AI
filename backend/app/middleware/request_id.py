import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class RequestIDMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        request_id = str(uuid.uuid4())

        start = time.perf_counter()

        request.state.request_id = request_id

        response = await call_next(request)

        duration = round(
            (time.perf_counter() - start) * 1000,
            2,
        )

        logger.bind(module="api").info(
            f"{request.method} "
            f"{request.url.path} "
            f"{response.status_code} "
            f"{duration} ms "
            f"{request_id}"
        )

        response.headers["X-Request-ID"] = request_id

        return response