"""
@author: jzaron
"""

from fetcher import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), index=True, unique=True)

    def __repr__(self):
        return '<URL {}>'.format(self.url)