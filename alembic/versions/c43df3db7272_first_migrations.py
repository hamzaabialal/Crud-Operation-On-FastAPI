"""first migrations

Revision ID: c43df3db7272
Revises: ad27cac2b227
Create Date: 2024-01-20 11:13:37.871728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c43df3db7272'
down_revision: Union[str, None] = 'ad27cac2b227'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
