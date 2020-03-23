"""
@author: jzaron
"""

import os

class AppConfig(object):
    APP_PORT = os.environ.get('APP_PORT') or '5000'