"""products

Revision ID: 3539df671205
Revises: 54c806a8b763
Create Date: 2025-10-06 02:21:41.482947

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3539df671205"
down_revision: Union[str, None] = "54c806a8b763"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("price", sa.Numeric(10, 2), nullable=False, server_default="0.00"),
        sa.Column("image", sa.String(255), nullable=True),
        sa.Column("description", sa.String(255), nullable=True),
        sa.Column("is_deleted", mysql.BIT(1), server_default=sa.text("b'0'")),
    )


def downgrade() -> None:
    op.drop_table("products")
