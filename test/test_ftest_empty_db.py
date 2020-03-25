"""
@author: jzaron
"""

import os
import tempfile

import pytest

from fetcher import app, db

EMPTY_RESPONSE = b'{}\n'

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['TESTING'] = True
    with app.test_client() as client:
        db.create_all()
        yield client
    os.close(db_fd)
    os.unlink(db_path)

def test_get_text(client):
    rv = client.get('/api/v1.0/content/image/fromSite?site=http://example.org')
    assert rv.data == EMPTY_RESPONSE

def test_list_images(client):
    rv = client.get('/api/v1.0/content/image/fromSite?site=http://example.org')
    assert rv.data == EMPTY_RESPONSE

def test_get_image(client):
    rv = client.get('/api/v1.0/content/image/get?id=1')
    assert rv.data == EMPTY_RESPONSE