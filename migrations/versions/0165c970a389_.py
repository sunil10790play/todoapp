"""empty message

Revision ID: 0165c970a389
Revises: 6e1d24366795
Create Date: 2022-05-17 16:12:17.542216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0165c970a389'
down_revision = '6e1d24366795'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
