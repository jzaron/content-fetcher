"""
@author: jzaron
"""

from fetcher import db

class Site(db.Model):
    __tablename__ = 'Site'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), index=True, unique=True)
    text = db.relationship('Text', backref='site', lazy=True)
    images = db.relationship('Image', backref='images', lazy=True)
    def __repr__(self):
        return f'<Site {self.url}>'