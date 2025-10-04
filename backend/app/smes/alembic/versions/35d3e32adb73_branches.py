"""branches

Revision ID: 35d3e32adb73
Revises: 60c0eac230fd
Create Date: 2025-10-04 04:16:23.291953

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "35d3e32adb73"
down_revision: Union[str, None] = "60c0eac230fd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "branches",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False, index=True
        ),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("address", sa.String(length=255)),
        sa.Column("is_deleted", mysql.BIT(1), server_default=sa.text("b'0'")),
    )


def downgrade():
    op.drop_table("branches")
