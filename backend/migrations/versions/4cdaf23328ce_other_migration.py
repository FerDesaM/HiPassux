"""Other migration

Revision ID: 4cdaf23328ce
Revises: af8376c1fbf2
Create Date: 2024-07-30 22:33:43.380407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cdaf23328ce'
down_revision = 'af8376c1fbf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend_requests',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('PENDING', 'ACCEPTED', 'REJECTED', name='requeststatus'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['USERS.user_id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['USERS.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friend_requests')
    # ### end Alembic commands ###
