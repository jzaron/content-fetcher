"""
@author: jzaron
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__) + '/..')

class Config(object):
    port = os.environ.get('APP_PORT') or '5000'
    STORAGE_BASE_URL = os.environ.get('STORAGE_DIR') or \
        os.path.join(basedir, 'storage')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(STORAGE_BASE_URL, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_QUEUE_NAME = 'content-fetcher-tasks'
