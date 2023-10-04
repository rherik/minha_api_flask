"""empty message

Revision ID: e516f98b4703
Revises: b880f64cc601
Create Date: 2023-10-03 20:44:21.025574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e516f98b4703'
down_revision = 'b880f64cc601'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False, server_default='lorem ipsum'))
        batch_op.drop_constraint('users_username_key', type_='unique')
        batch_op.create_unique_constraint('email', ['email'])
        batch_op.alter_column('email', server_default=None)
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint('email', type_='unique')
        batch_op.create_unique_constraint('users_username_key', ['username'])
        batch_op.drop_column('email')

    # ### end Alembic commands ###
