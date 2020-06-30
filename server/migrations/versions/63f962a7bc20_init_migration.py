"""Init migration

Revision ID: 63f962a7bc20
Revises: 
Create Date: 2020-06-29 22:38:20.727042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63f962a7bc20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('original_url', sa.Text(), nullable=False),
    sa.Column('code', sa.Text(), nullable=True),
    sa.Column('requested_count', sa.BigInteger(), server_default='0', nullable=False),
    sa.Column('used_count', sa.BigInteger(), server_default='0', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('original_url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    # ### end Alembic commands ###
