"""add vehicle name as unique constraint

Revision ID: f17157f38461
Revises: 952a48c52c76
Create Date: 2024-06-10 22:57:45.073462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f17157f38461'
down_revision: Union[str, None] = '952a48c52c76'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_vehicle_model', table_name='vehicle')
    op.create_index(op.f('ix_vehicle_model'), 'vehicle', ['model'], unique=True)
    op.create_unique_constraint('model_key', 'vehicle', ['model'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('model_key', 'vehicle', type_='unique')
    op.drop_index(op.f('ix_vehicle_model'), table_name='vehicle')
    op.create_index('ix_vehicle_model', 'vehicle', ['model'], unique=False)
    # ### end Alembic commands ###
