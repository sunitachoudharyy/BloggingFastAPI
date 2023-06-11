"""add few last columns to blogs table

Revision ID: 0c96a7482ba6
Revises: c6a920c4c04d
Create Date: 2023-06-09 23:08:10.148899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c96a7482ba6'
down_revision = 'c6a920c4c04d'
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('blogs', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('blogs', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('blogs', 'published')
    op.drop_column('blogs', 'created_at')
    pass
