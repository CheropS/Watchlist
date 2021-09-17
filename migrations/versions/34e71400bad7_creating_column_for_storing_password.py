"""creating column for storing password

Revision ID: 34e71400bad7
Revises: 
Create Date: 2021-09-17 11:36:40.472313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34e71400bad7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###