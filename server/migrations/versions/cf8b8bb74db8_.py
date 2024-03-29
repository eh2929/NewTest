"""empty message

Revision ID: cf8b8bb74db8
Revises: 
Create Date: 2024-03-21 09:43:02.120132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf8b8bb74db8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('username')
    )
    op.create_table('loan_applications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_address', sa.String(), nullable=True),
    sa.Column('borrower_id', sa.Integer(), nullable=True),
    sa.Column('loan_officer_id', sa.Integer(), nullable=True),
    sa.Column('real_estate_agent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['borrower_id'], ['users.id'], name=op.f('fk_loan_applications_borrower_id_users')),
    sa.ForeignKeyConstraint(['loan_officer_id'], ['users.id'], name=op.f('fk_loan_applications_loan_officer_id_users')),
    sa.ForeignKeyConstraint(['real_estate_agent_id'], ['users.id'], name=op.f('fk_loan_applications_real_estate_agent_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assigned_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assigned_date', sa.DateTime(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('loan_application_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loan_application_id'], ['loan_applications.id'], name=op.f('fk_assigned_tasks_loan_application_id_loan_applications')),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], name=op.f('fk_assigned_tasks_task_id_tasks')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('loan_application_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['loan_application_id'], ['loan_applications.id'], name=op.f('fk_comments_loan_application_id_loan_applications')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_comments_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('assigned_tasks')
    op.drop_table('loan_applications')
    op.drop_table('users')
    op.drop_table('tasks')
    # ### end Alembic commands ###
