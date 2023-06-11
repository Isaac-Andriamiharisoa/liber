"""empty message

Revision ID: b18f945d7691
Revises: 397a6c6d316d
Create Date: 2023-06-11 12:10:25.152912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18f945d7691'
down_revision = '397a6c6d316d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ames', sa.Column('contribution', sa.Integer(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ames', 'contribution')
    # ### end Alembic commands ###