"""empty message

Revision ID: aca188142924
Revises: 4c465483bf6c
Create Date: 2023-06-10 20:28:53.937124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aca188142924'
down_revision = '4c465483bf6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ames', 'mariage')
    op.drop_column('ames', 'fanavaozana')
    op.drop_column('ames', 'communion')
    op.drop_column('ames', 'confirmation')
    op.drop_column('ames', 'mort')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ames', sa.Column('mort', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('ames', sa.Column('confirmation', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('ames', sa.Column('communion', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('ames', sa.Column('fanavaozana', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('ames', sa.Column('mariage', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###