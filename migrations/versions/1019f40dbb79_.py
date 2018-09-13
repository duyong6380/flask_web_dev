"""empty message

Revision ID: 1019f40dbb79
Revises: f9bf3008dbeb
Create Date: 2018-09-13 03:33:18.413356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1019f40dbb79'
down_revision = 'f9bf3008dbeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updatetimestamp', sa.TIMESTAMP(timezone=True), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updatetimestamp')
    # ### end Alembic commands ###