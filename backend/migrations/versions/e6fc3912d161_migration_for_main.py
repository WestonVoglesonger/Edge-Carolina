"""Migration for main

Revision ID: e6fc3912d161
Revises: 1bbbbc97d715
Create Date: 2024-03-09 16:53:53.235198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6fc3912d161'
down_revision = '1bbbbc97d715'
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