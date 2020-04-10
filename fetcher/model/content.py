"""
@author: jzaron
"""

# TODO: extract common code

from fetcher import db


class Text(db.Model):
    __tablename__ = 'Text'
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('Site.id'),
        nullable=False)

    def __repr__(self):
        return f'<Text site_id:{self.site_id}>'


class Image(db.Model):
    __tablename__ = 'Image'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('Site.id'),
        nullable=False)

    def __repr__(self):
        return f'<Image url:{self.url}> site_id:{self.site_id}>'