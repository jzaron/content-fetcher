"""
@author: kuba
"""

from flask import Flask
from fetcher.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from fetcher import routes
from fetcher.model.base import URL
