"""
for sqlite uri format
sqlite:///current_file_path+db_name

postgres:
postgresql://user:pwd@host:port/db_name
"""

import os

class BaseConfig:
    db_name = 'my_db'
    user = 'postgres'
    password = '123456'
    port = '5432'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'postgresql://{user}:{password}@localhost:{port}/{db_name}'
