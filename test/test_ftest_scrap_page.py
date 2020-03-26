"""
@author: jzaron
"""

#TODO: ensure server with site up other way than sleep()
#TODO: add more tests

import http.server
import json
import os
from pathlib import Path
import pytest
import socketserver
import tempfile
from threading import Thread
from time import sleep

from fetcher import app, db

HTTPD_PORT = 18080
SITE = f'http://localhost:{HTTPD_PORT}/index.html'
WEB_DIR = Path(os.path.dirname(__file__)) / 'resources' / 'site1'

def run_httpd(httpd):
    httpd.serve_forever()

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

@pytest.fixture
def site():
    os.chdir(WEB_DIR)    
    Handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", HTTPD_PORT), Handler)
    thread = Thread(target = run_httpd, args = (httpd, ))
    thread.start()
    yield
    httpd.shutdown()
    httpd.server_close()

def test_scrap_page(client, site):
    sleep(1)
    client.put(f'/api/v1.0/content/text/scrapFromSite?site={SITE}')
    rv = client.get(f'/api/v1.0/content/text/fromSite?site={SITE}')
    reference = r'{"text": "\nTest heading\nTest paragraph\n"}'
    assert json.dumps(rv.get_json()) == reference

def test_scrap_images(client,site):
    sleep(1)
    client.put(f'/api/v1.0/content/image/scrapFromSite?site={SITE}')
    rv = client.get(f'/api/v1.0/content/image/fromSite?site={SITE}')
    reference = r'{"1": "http://localhost:18080/search.png", "2": "http://localhost:18080/mail.png"}'
    assert json.dumps(rv.get_json()) == reference
