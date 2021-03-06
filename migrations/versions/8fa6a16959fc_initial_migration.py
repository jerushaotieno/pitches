"""Initial Migration

Revision ID: 8fa6a16959fc
Revises: 537feddc1758
Create Date: 2022-03-10 15:33:36.956354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fa6a16959fc'
down_revision = '537feddc1758'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitches_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitches', ['pitches_id'], ['id'])
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'pitches_id')
    # ### end Alembic commands ###
