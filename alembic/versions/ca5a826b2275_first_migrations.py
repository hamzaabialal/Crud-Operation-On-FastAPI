"""first migrations

Revision ID: ca5a826b2275
Revises: c43df3db7272
Create Date: 2024-01-20 11:15:01.688813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca5a826b2275'
down_revision: Union[str, None] = 'c43df3db7272'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
