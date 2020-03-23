"""
@author: kuba
"""

#TODO: add logger

from flask import Flask

from flask_migrate import Migrate

from fetcher.config import Config
from fetcher.db import get_db
from fetcher.storage import get_storage

app = Flask(__name__)
app.config.from_object(Config)

db = get_db(Config, app)
migrate = Migrate(app, db)

storage = get_storage(Config)

from fetcher import routes
# from fetcher.model.base import URL
