"""Add Content Column to Posts Table

Revision ID: 2a3aa9a6a85c
Revises: 83cf8fef9b9d
Create Date: 2022-10-19 12:09:02.382376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a3aa9a6a85c'
down_revision = '83cf8fef9b9d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
