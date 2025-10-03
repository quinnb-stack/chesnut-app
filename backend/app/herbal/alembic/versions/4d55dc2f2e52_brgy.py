"""brgy

Revision ID: 4d55dc2f2e52
Revises: db4e83bfd5bd
Create Date: 2025-10-01 05:49:24.165868

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4d55dc2f2e52"
down_revision: Union[str, None] = "db4e83bfd5bd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "barangays",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("municipality", sa.String(150), nullable=False),
        sa.Column("captain_official", sa.Text, nullable=True),
        sa.Column(
            "is_deleted", mysql.BIT(1), nullable=False, server_default=sa.text("b'0'")
        ),
    )


def downgrade() -> None:
    op.drop_table("barangays")
