import hashlib
import hmac
import os


def hash_password(password: str) -> str:
    pepper = os.getenv("APP_PASSWORD_PEPPER", "ka-expense-pepper")
    return hashlib.sha256(f"{password}:{pepper}".encode("utf-8")).hexdigest()


def secure_compare(a: str, b: str) -> bool:
    return hmac.compare_digest(a, b)
