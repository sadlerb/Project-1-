"""empty message

Revision ID: 91c1eaca1aa1
Revises: e7f61c9234bf
Create Date: 2021-03-21 15:29:33.180888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91c1eaca1aa1'
down_revision = 'e7f61c9234bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('properties_photo_key', 'properties', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('properties_photo_key', 'properties', ['photo'])
    # ### end Alembic commands ###