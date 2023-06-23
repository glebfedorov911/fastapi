"""Add messages model

Revision ID: 106fa2276cbc
Revises: d9fd4744b8cb
Create Date: 2023-06-20 17:02:09.522392

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '106fa2276cbc'
down_revision = 'd9fd4744b8cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('operation')
    op.drop_table('role')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('permissions', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='role_pkey')
    )
    op.create_table('operation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('figi', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('instrument_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='operation_pkey')
    )
    op.drop_table('messages')
    # ### end Alembic commands ###