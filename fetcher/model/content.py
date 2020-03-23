"""
@author: jzaron
"""

from fetcher import db
from fetcher.model.base import URL

class Text(db.Model):
    __tablename__ = 'Text'
    id = db.Column(db.Integer, primary_key=True)
    storage_path = db.Column(db.String(512), nullable=False)
    url_id = db.Column(db.Integer, db.ForeignKey('URL.id'),
        nullable=False)

    def __repr__(self):
        return f'<Text storage_path:{self.storage_path} url:{self.url}>'