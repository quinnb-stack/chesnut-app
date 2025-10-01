"""herbal plants

Revision ID: db4e83bfd5bd
Revises: 8f092f628012
Create Date: 2025-10-01 03:31:52.321411

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "db4e83bfd5bd"
down_revision: Union[str, None] = "8f092f628012"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "herbal_plants",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("scientific_name", sa.String(255), nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("image_url", sa.String(255), nullable=True),
        sa.Column(
            "is_deleted", mysql.BIT(1), nullable=False, server_default=sa.text("b'0'")
        ),
    )


def downgrade() -> None:
    op.drop_table("herbal_plants")
