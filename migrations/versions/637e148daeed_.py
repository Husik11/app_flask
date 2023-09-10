"""empty message

Revision ID: 637e148daeed
Revises: 
Create Date: 2023-08-14 18:06:01.722732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '637e148daeed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=25), default='user'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###