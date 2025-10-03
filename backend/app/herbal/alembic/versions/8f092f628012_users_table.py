"""users table

Revision ID: 8f092f628012
Revises:
Create Date: 2025-09-29 06:25:14.156919

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8f092f628012"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("username", sa.String(25), nullable=False),
        sa.Column("password", sa.String(25), nullable=False),
        sa.Column(
            "role",
            sa.Enum("admin", "super_admin", name="user_roles"),
            nullable=False,
        ),
        sa.Column(
            "created_at", sa.TIMESTAMP, server_default=sa.func.current_timestamp()
        ),
        sa.Column("is_deleted", mysql.BIT(1), server_default=sa.text("b'0'")),
    )


def downgrade() -> None:
    op.drop_table("users")
