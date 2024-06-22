"""update sold vehicle, change user_id

Revision ID: 65d2d8f10398
Revises: 38567dcbd1da
Create Date: 2024-06-19 23:55:48.070069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '65d2d8f10398'
down_revision: Union[str, None] = '38567dcbd1da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    status_enum = postgresql.ENUM('draft', 'sold', name='status_enum')
    status_enum.create(op.get_bind())
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicle_sold', 'status',
               existing_type=postgresql.ENUM('draft', 'sold', name='status_enum'),
               type_=sa.Enum('draft', 'sold', name='status_enum'),
               existing_nullable=False)
    op.alter_column('vehicle_sold', 'user_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vehicle_sold', 'user_id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('vehicle_sold', 'status',
               existing_type=sa.Enum('draft', 'sold', name='status_enum'),
               type_=postgresql.ENUM('draft', 'sold', name='status_enum'),
               existing_nullable=False)
    # ### end Alembic commands ###
    status_enum = postgresql.ENUM('draft', 'sold', name='status_enum')
    status_enum.drop(op.get_bind())