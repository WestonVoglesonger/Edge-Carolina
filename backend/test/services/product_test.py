import pytest
from ...services.product import ProductService
from ...entities.product_entity import ProductEntity
from ...models.product_data import ProductData
from ...services.exceptions import (
    ResourceNotFoundException,
    ProductRegistrationException,
)
from .fixtures import product_service
from ..product_data import fake_data_fixture, product, new_product, updated_product


def test_get_products(product_service: ProductService) -> None:
    products = product_service.get_products()
    assert len(products) == 1 
    
def test_get_product(product_service: ProductService) -> None:
    product_id = 1
    product = product_service.get_product(product_id)
    assert product.id == product_id
    assert product.name == "Example Product"
    assert product.description == "This is a test product"
    assert product.github_url == "https://github.com/example/product"

def test_create_product(product_service: ProductService) -> None:
    created_product = product_service.create_product(new_product)
    assert created_product is not None
    assert created_product == new_product.id
    assert created_product.name == new_product.name
    assert created_product.description == new_product.description
    assert created_product.url == new_product.url

def test_create_product_existing_name(product_service: ProductService) -> None:
    with pytest.raises(ProductRegistrationException):
        product_service.create_product(product)

def test_update_product(product_service: ProductService) -> None:
    updated_product = product_service.update_product(updated_product)
    assert updated_product.name == updated_product.name
    assert updated_product.description == updated_product.description
    assert updated_product.url == updated_product.url

def test_update_product_non_existent(product_service: ProductService) -> None:
    with pytest.raises(ResourceNotFoundException):
        product_service.update_product(new_product)

def test_delete_product(product_service: ProductService) -> None:
    product_service.delete_product(1)
    with pytest.raises(ResourceNotFoundException):
        product_service.get_product(1)

def test_delete_product_non_existent(product_service: ProductService) -> None:
    with pytest.raises(ResourceNotFoundException):
        product_service.delete_product(999)

def test_get_product_by_id_not_found(product_service: ProductService) -> None:
    with pytest.raises(ResourceNotFoundException):
        product_service.get_product(999)
