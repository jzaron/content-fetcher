"""
@author: jzaron
"""

#TODO: refresh content
#TODO: errors handling

from fetcher import db, storage, scraper
from fetcher.model.base import URL
from fetcher.model.content import Text

def scrap_text(url):
    if not dbops.get_text(url):
        url_entry = dbops.get_or_create_url(url)
        storage_path = f'{url_entry.id}/text'
        text = scraper.get_text(url)
        storage.store_text(text, storage_path)
        dbops.put_text(storage_path, url_entry)
    return

def get_text(url):
    text_entry = dbops.get_text(url)
    if text_entry:
        return storage.load_text(text_entry.storage_path)
    return None
    
def scrap_images(url):
    #get images urls using scraper
    #download for each url, putting db entry
    return
    
def get_images(url):
    #list of streams, best if generator
    return []

class dbops(object):
    
    @staticmethod
    def put_text(storage_path, url_entry):
        text_entry = Text(storage_path = storage_path)
        url_entry.text.append(text_entry)
        db.session.add(text_entry)
        db.session.commit()

    @staticmethod
    def get_text(url):
        url_entry = dbops.get_url(url)
        if url_entry:
            try:
                text_entry = Text.query.with_parent(url_entry).one()
            except:
                return None
            else:
                return text_entry
        return None

    @staticmethod
    def get_or_create_url(url):
        url_entry = dbops.get_url(url)
        if not url_entry:
            url_entry = URL(url = url)
            db.session.add(url_entry)
            db.session.commit()
        return url_entry
    
    @staticmethod
    def get_url(url):
        try:
            url_entry = URL.query.filter(URL.url == url).one()
        except:
            return None
        else:
            return url_entry
        