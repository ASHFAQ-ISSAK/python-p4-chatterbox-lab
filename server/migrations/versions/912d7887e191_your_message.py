"""your message

Revision ID: 912d7887e191
Revises: 8e8d15410311
Create Date: 2023-06-22 11:07:37.918431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912d7887e191'
down_revision = '8e8d15410311'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('body', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('username', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('username')
        batch_op.drop_column('body')

    # ### end Alembic commands ###
