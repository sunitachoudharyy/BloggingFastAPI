"""add content column to blogs table

Revision ID: 9875dcf7594e
Revises: 9a280d191a5c
Create Date: 2023-06-07 23:37:09.880785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9875dcf7594e'
down_revision = '9a280d191a5c'
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column('blogs', sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() :
    op.drop_column('blogs','content')
    pass
