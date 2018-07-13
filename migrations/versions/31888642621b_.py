"""empty message

Revision ID: 31888642621b
Revises: e1adc6885ee7
Create Date: 2018-07-01 16:59:23.157768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31888642621b'
down_revision = 'e1adc6885ee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat_table',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('deal_id', sa.Integer(), nullable=True),
    sa.Column('speaker', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('chat_id')
    )
    op.create_table('deal_table',
    sa.Column('deal_id', sa.Integer(), nullable=False),
    sa.Column('lender_id', sa.Integer(), nullable=True),
    sa.Column('borrower_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('phase', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('deal_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deal_table')
    op.drop_table('chat_table')
    # ### end Alembic commands ###