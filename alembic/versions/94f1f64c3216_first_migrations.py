"""first migrations

Revision ID: 94f1f64c3216
Revises: accf8ce99a76
Create Date: 2024-01-20 11:02:54.543205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94f1f64c3216'
down_revision: Union[str, None] = 'accf8ce99a76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
