from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import db_session
from ..entities.product_entity import ProductEntity
from ..models.product_data import ProductData
from ..services.exceptions import (
    ResourceNotFoundException,
    ProductRegistrationException,
)
class ProductService:
    """Backend service that enables direct modification of product data."""

    def __init__(self, session: Session = Depends(db_session)):
        """Initializes the `ProductService` session"""
        self._session = session

    def get_products(self) -> list[ProductData]:
        """Retrieves all products."""
        query_result = self._session.query(ProductEntity).all()
        return [product_entity.to_model() for product_entity in query_result]

    def get_product(self, product_id: int) -> ProductData:
        """Gets one product by an ID."""
        product_entity = self._session.get(ProductEntity, product_id)
        if product_entity is None:
            raise ResourceNotFoundException("Product does not exist.")
        return product_entity.to_model()

    def create_product(self, product: ProductData) -> ProductData:
        """Stores a product in the database."""
        existing_product = self._session.query(ProductEntity).filter_by(url=product.url).first()
        if existing_product:
            raise ProductRegistrationException()
            
        new_product = ProductEntity.from_model(product)
        self._session.add(new_product)
        self._session.commit()
        return new_product.to_model()

    def update_product(self, product: ProductData) -> ProductData:
        """Modifies one product in the database."""
        product_entity = self._session.get(ProductEntity, product.id)
        if product_entity is None:
            raise ResourceNotFoundException("Product does not exist.")

        product_entity.name = product.name
        product_entity.description = product.description
        product_entity.url = product.url

        self._session.commit()
        return product_entity.to_model()

    def delete_product(self, product_id: int) -> None:
        """Deletes one product from the database."""
        product_entity = self._session.get(ProductEntity, product_id)
        if product_entity is None:
            raise ResourceNotFoundException("Product does not exist.")

        self._session.delete(product_entity)
        self._session.commit()
