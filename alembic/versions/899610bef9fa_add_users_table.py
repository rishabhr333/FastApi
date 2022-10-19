"""Add Users table

Revision ID: 899610bef9fa
Revises: 2a3aa9a6a85c
Create Date: 2022-10-19 12:13:57.252998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '899610bef9fa'
down_revision = '2a3aa9a6a85c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",sa.Column("id",sa.Integer(),nullable=False),
                            sa.Column("email",sa.String(),nullable=False),
                            sa.Column("password",sa.String(),nullable=False),
                            sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
                            sa.PrimaryKeyConstraint("id"),
                            sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
