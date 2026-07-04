"""Fix last_login timezone"""

from alembic import op
import sqlalchemy as sa

revision = "44b979adbab1"
down_revision = "1a9299fcd98c"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "users",
        "last_login",
        existing_type=sa.DateTime(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=True,
    )


def downgrade():
    op.alter_column(
        "users",
        "last_login",
        existing_type=sa.DateTime(timezone=True),
        type_=sa.DateTime(),
        existing_nullable=True,
    )