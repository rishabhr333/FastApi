"""Add Foreign Key to Posts Table

Revision ID: e9999234a7d8
Revises: 899610bef9fa
Create Date: 2022-10-19 12:23:50.379504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9999234a7d8'
down_revision = '899610bef9fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id",sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fkey", source_table="posts", referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fkey", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
