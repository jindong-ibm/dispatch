"""Adds plugin table

Revision ID: 895ae7783033
Revises: 057604415f6c
Create Date: 2020-04-14 16:52:08.628909

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = "895ae7783033"
down_revision = "1221a4d60f03"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "plugin",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("slug", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("version", sa.String(), nullable=True),
        sa.Column("author", sa.String(), nullable=True),
        sa.Column("author_url", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.Column("configuration", sqlalchemy_utils.types.json.JSONType(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )
    op.create_index(
        "ix_plugin_search_vector", "plugin", ["search_vector"], unique=False, postgresql_using="gin"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_plugin_search_vector", table_name="plugin")
    op.drop_table("plugin")
    # ### end Alembic commands ###
