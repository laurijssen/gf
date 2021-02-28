"""empty message

Revision ID: 61f8111782ac
Revises: b1028b262dfa
Create Date: 2021-02-28 08:00:33.339990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61f8111782ac'
down_revision = 'b1028b262dfa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
