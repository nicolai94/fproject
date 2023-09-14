"""del max length

Revision ID: fd0f53e8e28d
Revises: 2ba94597b6f9
Create Date: 2023-09-14 21:16:48.627945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fd0f53e8e28d"
down_revision: Union[str, None] = "2ba94597b6f9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_index("ix_model_items_id", table_name="model_items")
    op.drop_table("model_items")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "model_items",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="model_items_pkey"),
    )
    op.create_index("ix_model_items_id", "model_items", ["id"], unique=False)
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("full_name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("disabled", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
    )
    # ### end Alembic commands ###