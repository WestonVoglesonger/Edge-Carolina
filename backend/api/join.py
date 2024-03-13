"""Productivity API

Productivity routes are used to create, retrieve, and update Pomodoro timers."""

from fastapi import APIRouter, Depends

from backend.models.admin_data import AdminData
from backend.services.exceptions import AdminRegistrationException
from ..services.join import JoinService


api = APIRouter(prefix="/api/join")
openapi_tags = {
    "name": "Join",
    "description": "Create, update, delete, and retrieve admin data.",
}


# GET /api/join
# Gets all admins.
# Expected return type: list[AdminData]
@api.get("", response_model=list[AdminData], tags=["Join"])
def get_admins(
    join_service: JoinService = Depends(),
) -> list[AdminData]:
    """
    Get all admins.

    Parameters:
        join_service: a valid JoinService

    Returns:
        list[AdminData]: All admins
    """

    # Return all admins
    return join_service.get_admins()


# GET /api/join/{id}
# Get a admin by its ID.
# Expected return type: AdminData
@api.get("/{id}", response_model=AdminData, tags=["Join"])
def get_admin(
    id: int,
    join_service: JoinService = Depends(),
) -> AdminData:
    """
    Get admin.

    Parameters:
        id: ID of the admin to get
        join_service: a valid JoinService
    """

    return join_service.get_admin(id)


# POST /api/join/
# Creates a new admin.
# Expected return type: AdminData
@api.post("", response_model=AdminData, tags=["Join"])
def create_admin(
    admin: AdminData,
    join_service: JoinService = Depends(),
) -> AdminData:
    """
    Create admin.

    Parameters:
        admin: a valid admin model
        join_service: a valid JoinService

    Returns:
        admin: Created admin
    """

    return join_service.create_admin(admin)


# PUT /api/join
# Updates a admin.
# Expected return type: AdminData
@api.put("", response_model=AdminData, tags=["Join"])
def update_admin(
    admin: AdminData,
    join_service: JoinService = Depends(),
) -> AdminData:
    """
    Update admin.

    Parameters:
        admin: a valid AdminData model
        admin_service: a valid JoinService

    Returns:
        AdminData: Updated admin
    """

    return join_service.update_admin(admin)


# DELETE /api/productivity/{id}
# Deletes a admin.
# Expected return type: AdminData
@api.delete("/{id}", response_model=None, tags=["Join"])
def delete_admin(
    id: int,
    join_service: JoinService = Depends(),
) -> AdminData:
    """
    Delete admin.

    Parameters:
        id: ID of the admin to delete
        join_service: a valid JoinService
    """

    return join_service.delete_admin(id) # type: ignore

@api.get("/check-email/{email}", response_model=bool)
def check_email_registered(email: str, join_service: JoinService = Depends()) -> bool:
    """
    Check if an email is already registered.

    Parameters:
        email: Email to check

    Returns:
        bool: True if email is registered, False otherwise
    """
    return join_service.check_email_registered(email)