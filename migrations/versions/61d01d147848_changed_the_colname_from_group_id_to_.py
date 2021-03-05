"""Changed the colname from group_id to posted_server_id

Revision ID: 61d01d147848
Revises: dc08c503dc3b
Create Date: 2021-03-05 07:01:51.879226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61d01d147848'
down_revision = 'dc08c503dc3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('posted_server_id', sa.String(length=50), nullable=True))
    op.drop_column('results', 'group_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('group_id', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_column('results', 'posted_server_id')
    # ### end Alembic commands ###
