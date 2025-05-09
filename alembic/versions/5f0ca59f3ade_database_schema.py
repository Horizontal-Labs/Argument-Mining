"""Database Schema

Revision ID: 5f0ca59f3ade
Revises: 
Create Date: 2025-04-30 15:49:34.048751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f0ca59f3ade'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('domain',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain_name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('type', sa.String(length=16), nullable=False),
    sa.Column('domain_id', sa.Integer(), nullable=False),
    sa.CheckConstraint("type IN ('premise', 'claim')", name='check_type_valid'),
    sa.ForeignKeyConstraint(['domain_id'], ['domain.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relationship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_adu_id', sa.Integer(), nullable=False),
    sa.Column('to_adu_id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=16), nullable=False),
    sa.Column('domain_id', sa.Integer(), nullable=False),
    sa.CheckConstraint("category IN ('support', 'stance_pro', 'stance_con')", name='check_category_valid'),
    sa.ForeignKeyConstraint(['domain_id'], ['domain.id'], ),
    sa.ForeignKeyConstraint(['from_adu_id'], ['adu.id'], ),
    sa.ForeignKeyConstraint(['to_adu_id'], ['adu.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relationship')
    op.drop_table('adu')
    op.drop_table('domain')
    # ### end Alembic commands ###
