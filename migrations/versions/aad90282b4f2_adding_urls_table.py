"""Adding URLs table.

Revision ID: aad90282b4f2
Revises: 
Create Date: 2020-03-23 17:17:48.322934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aad90282b4f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URL',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_URL_url'), 'URL', ['url'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_URL_url'), table_name='URL')
    op.drop_table('URL')
    # ### end Alembic commands ###
