"""users

Revision ID: 2a0265fd902e
Revises:
Create Date: 2025-10-04 01:47:09.853941

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2a0265fd902e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(25), nullable=False),
        sa.Column("password", sa.String(25), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("contact", sa.String(255), nullable=False),
        sa.Column("address", sa.String(255), nullable=False),
        sa.Column(
            "role",
            sa.Enum(
                "branch_admin", "super_admin", "customer", "rider", name="user_roles"
            ),
            nullable=False,
        ),
        sa.Column(
            "created_at", sa.TIMESTAMP, server_default=sa.func.current_timestamp()
        ),
        sa.Column("is_deleted", mysql.BIT(1), server_default=sa.text("b'0'")),
    )


def downgrade() -> None:
    op.drop_table("users")
