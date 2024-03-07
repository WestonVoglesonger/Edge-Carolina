"""Mock data for products."""


import pytest
from sqlalchemy.orm import Session
from backend.entities.product_entity import ProductEntity

from backend.models.product_data import ProductData
from backend.test.services.reset_table_id_seq import reset_table_id_seq

__authors__ = ["Weston Voglesonger"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

product_1 = ProductData(
    id=1,
    name="Example Product",
    description="This is a test product",
    url="https://github.com/example/product"
)

new_product = ProductData(
    id=2,
    name="product",
    description="product",
    url="https://github.com/test/repo"
)

updated_product = ProductData(
    id=1,
    name="Updated Product",
    description="This product has been updated",
    url="https://github.com/example/updated-product"
)

products = [product_1]


def insert_fake_data(session: Session):
    global products
    entities = []
    for product in products:
        entity = ProductEntity.from_model(product)
        session.add(entity)
        entities.append(entity)
    reset_table_id_seq(session, ProductEntity, ProductEntity.id, len(products) + 1)
    session.commit()  # Commit to ensure Product IDs in database


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
