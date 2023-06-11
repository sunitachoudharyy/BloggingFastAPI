"""add foreign key to blogs table

Revision ID: c6a920c4c04d
Revises: 4f92bc36ec9c
Create Date: 2023-06-09 17:34:38.362026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6a920c4c04d'
down_revision = '4f92bc36ec9c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('blogs', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('blog_users_fk', source_table="blogs", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('blog_users_fk', table_name="blogs")
    op.drop_column('blogs', 'owner_id')
    pass
