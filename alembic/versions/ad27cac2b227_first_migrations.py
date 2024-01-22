"""first migrations

Revision ID: ad27cac2b227
Revises: 94f1f64c3216
Create Date: 2024-01-20 11:03:46.149185

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad27cac2b227'
down_revision: Union[str, None] = '94f1f64c3216'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
