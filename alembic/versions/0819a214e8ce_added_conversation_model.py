"""added conversation model

Revision ID: 0819a214e8ce
Revises: 
Create Date: 2021-05-07 20:46:12.961049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0819a214e8ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('participants_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vk_id', sa.String(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('surname', sa.Text(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_whitelisted', sa.Boolean(), nullable=True),
    sa.Column('join_date', sa.Date(), nullable=True),
    sa.Column('conversation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('conversation')
    # ### end Alembic commands ###