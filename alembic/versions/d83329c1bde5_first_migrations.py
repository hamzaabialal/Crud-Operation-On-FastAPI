"""first migrations

Revision ID: d83329c1bde5
Revises: ca5a826b2275
Create Date: 2024-01-20 11:21:36.217245

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd83329c1bde5'
down_revision: Union[str, None] = 'ca5a826b2275'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
