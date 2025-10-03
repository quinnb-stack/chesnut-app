"""plant_geotags

Revision ID: b18d7e60e1c4
Revises: 4d55dc2f2e52
Create Date: 2025-10-01 06:31:07.471043

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b18d7e60e1c4"
down_revision: Union[str, None] = "4d55dc2f2e52"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "plant_geotags",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "plant_id", sa.Integer, sa.ForeignKey("herbal_plants.id"), nullable=False
        ),
        sa.Column("brgy_id", sa.Integer, sa.ForeignKey("barangays.id"), nullable=False),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("latitude", sa.Numeric(10, 8), nullable=False),
        sa.Column("longitude", sa.Numeric(11, 8), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("plant_geotags")
