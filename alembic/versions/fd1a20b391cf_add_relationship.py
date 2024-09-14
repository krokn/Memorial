"""add relationship

Revision ID: fd1a20b391cf
Revises: d903d955503a
Create Date: 2024-09-13 19:57:05.010338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd1a20b391cf'
down_revision: Union[str, None] = 'd903d955503a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('educationInstitution', 'name',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.add_column('post', sa.Column('idUser', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'post', 'user', ['idUser'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'idUser')
    op.alter_column('educationInstitution', 'name',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###