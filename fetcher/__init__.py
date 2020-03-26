"""
@author: kuba
"""

#TODO: add logger
#TODO: make redis connection configurable

from flask import Flask
from flask_migrate import Migrate
from redis import Redis
import rq

from fetcher.config import Config
from fetcher.db import get_db
from fetcher.storage import get_storage

app = Flask(__name__)
app.config.from_object(Config)

db = get_db(Config, app)
migrate = Migrate(app, db)

storage = get_storage(Config)

app.redis = Redis()
app.task_queue = rq.Queue('content-fetcher-tasks', connection=app.redis)

from fetcher import routes
# from fetcher.model.base import URL
