import http.server
from pathlib import Path
import socketserver
import os
from threading import Thread, Event
from time import sleep


def run_httpd(httpd):
    httpd.serve_forever()


if __name__ == "__main__":
    PORT = 8000
    
    web_dir = Path(os.path.dirname(__file__)) / 'resources' / 'site1'
    os.chdir(web_dir)
    
    Handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        thread = Thread(target = run_httpd, args = (httpd, ))
        thread._stop_event = Event()
        thread.daemon = True
        thread.start()
        sleep(1800)
        httpd.shutdown()
