import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', '')))

from app import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from models.index.index import *
from models.sys_dashboard.sys_dashboard import *
