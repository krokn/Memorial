"""change name column

Revision ID: 8fe0c16c0601
Revises: fd1a20b391cf
Create Date: 2024-09-14 09:18:41.292903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fe0c16c0601'
down_revision: Union[str, None] = 'fd1a20b391cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(), nullable=False))
    op.add_column('post', sa.Column('content', sa.String(), nullable=False))
    op.alter_column('post', 'linkToPhoto',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_column('post', 'description')
    op.drop_column('post', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('post', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('post', 'linkToPhoto',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.drop_column('post', 'content')
    op.drop_column('post', 'title')
    # ### end Alembic commands ###
