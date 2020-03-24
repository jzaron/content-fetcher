"""
@author: jzaron
"""

#TODO: switch to streams
#TODO: would be nice to implement driver for HDFS, AWS S3, etc.

from pathlib import Path
import requests

def get_storage(config):
    return FileSystemStorage(config.STORAGE_BASE_URL)
    

class Storage(object):
    def put_text(self, text: str, path: str):
        pass

    def get_text(self, path: str) -> str:
        pass
        
    def put_image(self, url: str, path: str):
        pass

    def get_image(self, path: str) -> str:
        pass

class FileSystemStorage(Storage):

    def __init__(self, storage_root):
        self._storage_root = Path(storage_root)
        self._storage_root.mkdir(parents=True, exist_ok=True)
        
    def put_text(self, text, path):
        full_path = self.get_full_path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(text)

    def get_text(self, path):
        full_path = self.get_full_path(path)
        with open(full_path, 'r') as f:
            return f.read()

    def put_image(self, url, path):
        full_path = self.get_full_path(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'wb') as f:
            response = requests.get(url)
            f.write(response.content)

    def get_image(self, path):
        full_path = self.get_full_path(path)
        return full_path
    
    def get_full_path(self, path):
        return self._storage_root / path
    