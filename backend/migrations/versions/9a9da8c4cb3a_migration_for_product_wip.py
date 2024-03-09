"""Migration for product-WIP

Revision ID: 9a9da8c4cb3a
Revises: 44c13d40bcad
Create Date: 2024-03-07 14:30:02.425139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a9da8c4cb3a'
down_revision = '44c13d40bcad'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=100), nullable=False),
        sa.Column('url', sa.String(length=2083), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('url')
    )

def downgrade() -> None:
    op.drop_table('product')
