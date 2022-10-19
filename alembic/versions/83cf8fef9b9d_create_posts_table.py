"""create posts table

Revision ID: 83cf8fef9b9d
Revises: 
Create Date: 2022-10-18 00:35:32.132352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83cf8fef9b9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
