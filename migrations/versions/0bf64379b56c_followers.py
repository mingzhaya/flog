"""followers

Revision ID: 0bf64379b56c
Revises: 287ec56bb96c
Create Date: 2020-07-23 19:50:12.200921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bf64379b56c'
down_revision = '287ec56bb96c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
