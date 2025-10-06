"""riders

Revision ID: 54c806a8b763
Revises: 35d3e32adb73
Create Date: 2025-10-04 05:28:18.603406

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "54c806a8b763"
down_revision: Union[str, None] = "35d3e32adb73"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "riders",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "branch_id",
            sa.Integer,
            sa.ForeignKey("branches.id"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
        ),
        sa.Column("is_deleted", mysql.BIT(1), server_default=sa.text("b'0'")),
    )


def downgrade():
    op.drop_table("riders")
