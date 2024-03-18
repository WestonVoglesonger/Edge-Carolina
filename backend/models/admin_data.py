"""Pydantic Model for Admin data."""

from pydantic import BaseModel


class AdminData(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    email: str
    hashed_password: str
<<<<<<< HEAD:backend/models/admin_data.py
=======
    major: str
>>>>>>> 90357f1 (Added password field to user_data and password column to user_entity.):backend/models/user_data.py
