"""Initial Migration

Revision ID: 4294397f54fd
Revises: 736bf4c8d3ae
Create Date: 2022-03-07 07:52:37.660171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4294397f54fd'
down_revision = '736bf4c8d3ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'password_encrypt')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_encrypt', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###