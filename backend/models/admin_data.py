"""Pydantic Model for Admin data."""

from pydantic import BaseModel


class AdminData(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    email: str
    hashed_password: str
