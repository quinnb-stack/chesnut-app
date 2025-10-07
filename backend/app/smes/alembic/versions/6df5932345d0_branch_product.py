"""branch product

Revision ID: 6df5932345d0
Revises: 3539df671205
Create Date: 2025-10-06 05:05:16.753474

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6df5932345d0"
down_revision: Union[str, None] = "3539df671205"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "branch_products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "product_id", sa.Integer, sa.ForeignKey("products.id"), nullable=False
        ),
        sa.Column(
            "branch_id", sa.Integer, sa.ForeignKey("branches.id"), nullable=False
        ),
        sa.Column("quantity", sa.Integer, nullable=False, server_default="0"),
    )


def downgrade() -> None:
    op.drop_table("branch_products")
