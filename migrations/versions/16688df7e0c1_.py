"""empty message

Revision ID: 16688df7e0c1
Revises: ce0c8ab4d716
Create Date: 2023-01-03 08:55:46.574375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16688df7e0c1'
down_revision = 'ce0c8ab4d716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ames', sa.Column('password', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ames', 'password')
    # ### end Alembic commands ###
