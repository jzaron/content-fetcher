"""
@author: jzaron
"""

from fetcher import db

class URL(db.Model):
    __tablename = 'URL'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), index=True, unique=True)
    text = db.relationship('Text', backref='url', lazy=True)
    def __repr__(self):
        return f'<URL {self.url}>'