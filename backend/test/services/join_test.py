import pytest
from ...services.join import JoinService
from ...entities.admin_entity import AdminEntity
from ...models.admin_data import AdminData
from ...services.exceptions import (
    ResourceNotFoundException,
    AdminRegistrationException,
)
from .fixtures import join_service
from ..admin_data import fake_data_fixture, updated_root, admin


def test_get_admins(join_service: JoinService) -> None:
    admins = join_service.get_admins()
    assert len(admins) == 1 
    
def test_get_admin(join_service: JoinService) -> None:
    admin_id = 1
    admin = join_service.get_admin(admin_id)
    assert admin.id == admin_id
    assert admin.first_name == "root"
    assert admin.last_name == "root"
    assert admin.email == "root@unc.edu"
    assert admin.hashed_password == "password"

def test_create_admin(join_service: JoinService) -> None:
    created_admin = join_service.create_admin(admin)
    assert created_admin.email == admin.email

def test_create_admin_existing_email(join_service: JoinService) -> None:
    with pytest.raises(AdminRegistrationException):
        join_service.create_admin(updated_root)

def test_update_admin(join_service: JoinService) -> None:
    updated_admin = join_service.update_admin(updated_root)
    assert updated_admin.first_name == "updated"
    assert updated_admin.last_name == "updated"

def test_update_admin_non_existent(join_service: JoinService) -> None:
    with pytest.raises(ResourceNotFoundException):
        join_service.update_admin(admin)

def test_delete_admin(join_service: JoinService) -> None:
    join_service.delete_admin(1)
    with pytest.raises(ResourceNotFoundException):
        join_service.get_admin(1)

def test_delete_admin_non_existent(join_service: JoinService) -> None:
    with pytest.raises(ResourceNotFoundException):
        join_service.delete_admin(999)

def test_get_admin_by_id_not_found(join_service: JoinService) -> None:
    with pytest.raises(ResourceNotFoundException):
        join_service.get_admin(999)

def test_check_email_registered(join_service: JoinService) -> None:
    assert join_service.check_email_registered("root@unc.edu") is True
    assert join_service.check_email_registered("nonexistent@example.com") is False
