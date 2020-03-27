import os

DEBUG = True
SECRET_KEY = 'abc123'
STATIC_F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/')
CACHE_TYPE = "null"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:unlock@localhost:5432/test_bench'
TEMPLATES_AUTO_RELOAD = True