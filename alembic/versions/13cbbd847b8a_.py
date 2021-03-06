"""empty message

Revision ID: 13cbbd847b8a
Revises: 0819a214e8ce
Create Date: 2021-05-27 12:52:20.747680

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '13cbbd847b8a'
down_revision = '0819a214e8ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('participants_number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('auth_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vk_id', sa.String(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('surname', sa.Text(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_whitelisted', sa.Boolean(), nullable=True),
    sa.Column('join_date', sa.Date(), nullable=True),
    sa.Column('conversation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['auth_conversation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    op.drop_table('conversation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conversation',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('conversation_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('participants_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='conversation_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('vk_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('surname', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_whitelisted', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('join_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('conversation_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['conversation_id'], ['conversation.id'], name='user_conversation_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('auth_user')
    op.drop_table('auth_conversation')
    # ### end Alembic commands ###
