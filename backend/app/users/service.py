from app.services.base import BaseService


class UserService(BaseService):

    async def get_profile(
        self,
        user,
    ):
        return user