import sqlalchemy as sa

meta = sa.MetaData()

user = sa.Table(
    'user', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('mail', sa.String(200), nullable=False),
    sa.Column('password', sa.String, nullable=False),

    # Indexes #
    sa.PrimaryKeyConstraint('id', name='user_id'))
