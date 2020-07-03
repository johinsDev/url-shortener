"""Add last request and used count

Revision ID: ea193aa361aa
Revises: e6b3e103b87b
Create Date: 2020-07-03 15:46:27.298849

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ea193aa361aa'
down_revision = 'e6b3e103b87b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('links', sa.Column(
        'last_requested', sa.DateTime(), nullable=True))
    op.add_column('links', sa.Column(
        'last_used', sa.DateTime(), nullable=True))
    op.alter_column('links', 'created',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True)
    op.alter_column('links', 'updated',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('links', 'updated',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True)
    op.alter_column('links', 'created',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True)
    op.drop_column('links', 'last_used')
    op.drop_column('links', 'last_requested')
    # ### end Alembic commands ###
