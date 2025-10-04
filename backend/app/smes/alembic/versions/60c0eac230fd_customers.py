"""customers

Revision ID: 60c0eac230fd
Revises: 2a0265fd902e
Create Date: 2025-10-04 02:05:10.242644

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "60c0eac230fd"
down_revision: Union[str, None] = "2a0265fd902e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("behavioral_score", sa.Numeric(5, 2), default=0.00),
        sa.Column("cancel_count", sa.Integer, default=0),
    )


def downgrade():
    op.drop_table("customers")
