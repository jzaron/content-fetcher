"""Added Task table.

Revision ID: 1de22960d67b
Revises: 1de1bbc79788
Create Date: 2020-03-26 20:14:42.048322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1de22960d67b'
down_revision = '1de1bbc79788'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Task',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('category', sa.String(length=32), nullable=True),
    sa.Column('finished', sa.Boolean(), nullable=True),
    sa.Column('site_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['site_id'], ['Site.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Task_category'), 'Task', ['category'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Task_category'), table_name='Task')
    op.drop_table('Task')
    # ### end Alembic commands ###