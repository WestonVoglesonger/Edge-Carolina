"""Pydantic Model for User data."""

from pydantic import BaseModel


class UserData(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    major: str
