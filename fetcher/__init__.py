"""
@author: jzaron
"""

# TODO: add logger

from flask import Flask
from flask_migrate import Migrate
from redis import Redis
from rq import Queue

from fetcher.config import Config
from fetcher.db import get_db
from fetcher.storage import get_storage

app = Flask(__name__)
app.config.from_object(Config)

db = get_db(Config, app)
migrate = Migrate(app, db)

storage = get_storage(Config)

app.redis = Redis()
app.task_queue = Queue(Config.REDIS_QUEUE_NAME, connection=app.redis)

from fetcher import routes
