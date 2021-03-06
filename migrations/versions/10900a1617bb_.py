"""empty message

Revision ID: 10900a1617bb
Revises: 61f8111782ac
Create Date: 2021-03-14 12:28:39.786227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10900a1617bb'
down_revision = '61f8111782ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
