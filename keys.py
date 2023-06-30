import os

__all__ = (
    'CLIENT_ID',
    'SECRET_KEY',
    'USERNAME',
    'PASSWORD',
)


CLIENT_ID: str = os.environ['REDDIT_API_CLIENT_ID']
SECRET_KEY: str = os.environ['REDDIT_API_SECRET_KEY']
USERNAME: str = os.environ['REDDIT_API_USERNAME']
PASSWORD: str = os.environ['REDDIT_API_PASSWORD']
