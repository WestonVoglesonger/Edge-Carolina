from typing import Generator
import pytest
from sqlalchemy.orm import Session
from ...services import (
    ProductService,
    AdminService

)


__authors__ = ["Weston Voglesonger"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

@pytest.fixture()
def admin_service(session: Session):
    """Fixture to provide an instance of AdminService with a mock session."""
    return AdminService(session=session)


@pytest.fixture()
def product_service(session: Session):
    """Fixture to provide an instance of ProductService with a mock session."""
    return ProductService(session=session)

