"""add department support

Revision ID: 25b14f4b9080
Revises: 4474872b0ee6
Create Date: 2025-06-18 08:53:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '25b14f4b9080'
down_revision = '4474872b0ee6'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('tenant_account_joins', schema=None) as batch_op:
        batch_op.add_column(sa.Column('department', sa.String(length=255), nullable=True))
    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.add_column(sa.Column('department', sa.String(length=255), nullable=True))


def downgrade():
    with op.batch_alter_table('apps', schema=None) as batch_op:
        batch_op.drop_column('department')
    with op.batch_alter_table('tenant_account_joins', schema=None) as batch_op:
        batch_op.drop_column('department')
