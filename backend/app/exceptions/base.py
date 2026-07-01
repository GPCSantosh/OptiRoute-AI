from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
    ):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )


class BadRequestException(BaseAPIException):
    def __init__(self, detail: str = "Bad Request"):
        super().__init__(
            status.HTTP_400_BAD_REQUEST,
            detail,
        )


class UnauthorizedException(BaseAPIException):
    def __init__(self, detail: str = "Unauthorized"):
        super().__init__(
            status.HTTP_401_UNAUTHORIZED,
            detail,
        )


class ForbiddenException(BaseAPIException):
    def __init__(self, detail: str = "Forbidden"):
        super().__init__(
            status.HTTP_403_FORBIDDEN,
            detail,
        )


class NotFoundException(BaseAPIException):
    def __init__(self, detail: str = "Resource Not Found"):
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            detail,
        )


class ConflictException(BaseAPIException):
    def __init__(self, detail: str = "Conflict"):
        super().__init__(
            status.HTTP_409_CONFLICT,
            detail,
        )


class InternalServerException(BaseAPIException):
    def __init__(self):
        super().__init__(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Internal Server Error",
        )