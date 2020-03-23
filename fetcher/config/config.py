"""
@author: jzaron
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__) + '/..')

class Config(object):
    port = os.environ.get('APP_PORT') or '5000'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
