"""
@author: jzaron
"""

from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

#TODO: allow integration with different databases than SQLite 

def get_db(config, app):
    Path(config.STORAGE_BASE_URL).mkdir(parents=True, exist_ok=True)
    return SQLAlchemy(app)