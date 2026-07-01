from passlib.context import CryptContext

# Password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


class PasswordManager:
    """
    Handles password hashing and verification.
    """

    @staticmethod
    def hash(password: str) -> str:
        """
        Hash a plain-text password.
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify(
        plain_password: str,
        hashed_password: str,
    ) -> bool:
        """
        Verify a plain password against a hash.
        """
        return pwd_context.verify(
            plain_password,
            hashed_password,
        )