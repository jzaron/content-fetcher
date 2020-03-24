"""
@author: jzaron
"""

#TODO: refresh content
#TODO: errors handling

from fetcher import db, storage, scraper
from fetcher.model.base import Site
from fetcher.model.content import Text, Image

def scrap_text(site):
    if not db_entries.get_text(site):
        text = scraper.get_text(site)
        site_entry = db_entries.get_or_put_site(site)
        storage_path = get_text_path(site_entry.id)
        storage.put_text(text, storage_path)
        db_entries.put_text(site_entry)
        db.session.commit()

def get_text(site):
    text_entry = db_entries.get_text(site)
    if text_entry:
        return storage.get_text(get_text_path(text_entry.site_id))
    return None

def get_text_path(site_id):
    return f'{site_id}/text'
    
def scrap_images(site):
    site_entry = db_entries.get_or_put_site(site)
    urls = scraper.get_image_urls(site)
    for url in urls:
        image_entry = db_entries.put_image(url, site_entry)
        storage_path = get_image_path(site_entry.id, image_entry.id)
        storage.put_image(url, storage_path)
        db.session.commit()
    
def list_images(site):
    #list of streams, best if generator
    image_entries = db_entries.get_images(db_entries.get_site(site))
    if image_entries:
        return {i.id:i.url for i in image_entries}
    return {}

def get_image(id):
    image_entry = db_entries.get_image(id)
    if image_entry:
        return storage.get_image(get_image_path(image_entry.site_id, image_entry.id))
    return None

def get_image_path(site_id, image_id):
    return f'{site_id}/{image_id}'

class db_entries(object):
    
    @staticmethod
    def put_text(site_entry):
        text_entry = Text()
        site_entry.text.append(text_entry)
        db.session.add(text_entry)
        db.session.flush()
        return text_entry

    @staticmethod
    def get_text(site):
        site_entry = db_entries.get_site(site)
        if site_entry:
            try:
                text_entry = Text.query.with_parent(site_entry).one()
            except:
                return None
            else:
                return text_entry
        return None

    @staticmethod
    def put_image(url, site_entry):
        image_entry = Image(url = url)
        site_entry.images.append(image_entry)
        db.session.add(image_entry)
        db.session.flush()
        return image_entry

    @staticmethod
    def get_image(id):
        try:
            image_entry = Image.query.get(id)
        except:
            return None
        else:
            return image_entry
        return None

    @staticmethod
    def get_images(site_entry):
        if site_entry:
            try:
                image_entries = Image.query.with_parent(site_entry).all()
            except:
                return None
            else:
                return image_entries
        return None

    @staticmethod
    def get_or_put_site(url):
        site_entry = db_entries.get_site(url)
        if not site_entry:
            site_entry = Site(url = url)
            db.session.add(site_entry)
            db.session.flush()
        return site_entry
    
    @staticmethod
    def get_site(url):
        try:
            site_entry = Site.query.filter(Site.url == url).one()
        except:
            return None
        else:
            return site_entry
        