"""Update Columns of the Post Table

Revision ID: 7fda0d332f40
Revises: e9999234a7d8
Create Date: 2022-10-19 12:31:45.983639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fda0d332f40'
down_revision = 'e9999234a7d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published",sa.Boolean(),server_default='TRUE',nullable=False))
    op.add_column("posts", sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
