"""update role.permissions

Revision ID: e607412a47e2
Revises: 
Create Date: 2017-09-08 12:51:36.391201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e607412a47e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_unique_constraint(None, 'roles', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'roles', type_='unique')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'name')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
