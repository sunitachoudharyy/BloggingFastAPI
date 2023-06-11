"""create blogs table

Revision ID: 9a280d191a5c
Revises: 
Create Date: 2023-06-07 23:09:40.112512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a280d191a5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() :
    op.create_table('blogs', sa.Column('id', sa.Integer(),nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('blogs')
    pass
