"""add user table

Revision ID: 4f92bc36ec9c
Revises: 9875dcf7594e
Create Date: 2023-06-09 17:00:51.234659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f92bc36ec9c'
down_revision = '9875dcf7594e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(),nullable=False),
                    sa.Column('email', sa.String(),nullable=False),
                    sa.Column('password', sa.String(),nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
                    
    pass


def downgrade():
    op.drop_table("users")
    pass
