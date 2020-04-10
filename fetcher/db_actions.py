"""
@author: jzaron
"""

from fetcher.model.base import Site, Task
from fetcher.model.content import Image, Text

# TODO: THIS IS TO REWORK
# TODO: Such methods should be binded to model classes, they are for now like this because of the need to operate on db
# in RQ tasks. The approach should be reworked to avoid any db actions in RQ tasks. In case of need to signalize a task
# has finished, a HTTP request should be sent to the application using dedicated REST API endpoint, so only the
# application will handle database operations.


class DbActions(object):

    def __init__(self, db):
        self._db = db

    def put_text(self, site_entry):
        text_entry = Text()
        site_entry.text.append(text_entry)
        self._db.session.add(text_entry)
        self._db.session.commit()
        return text_entry

    def get_text_by_id(self, text_id):
        try:
            return self._db.session.query(Text).get(text_id)
        except:
            return None

    def put_image(self, site_entry, url):
        image_entry = Image(url = url)
        site_entry.images.append(image_entry)
        self._db.session.add(image_entry)
        self._db.session.commit()
        return image_entry

    def get_image_by_id(self, image_id):
        try:
            return self._db.session.query(Image).get(image_id)
        except:
            return None

    def put_task(self, site_entry, task_id, category):
        task_entry = Task(id = task_id, category = category)
        site_entry.tasks.append(task_entry)
        self._db.session.add(task_entry)
        self._db.session.commit()
        return task_entry

    def get_task_by_site_and_category(self, site_entry, category):
        try:
            return self._db.session.query(Task).with_parent(site_entry).filter(
                Task.category == category).one_or_none()
        except:
            return None

    def get_task_by_id(self, task_id):
        try:
            return self._db.session.query(Task).get(task_id)
        except:
            return None

    def get_or_put_site(self, url):
        site_entry = self.get_site_by_url(url)
        if not site_entry:
            site_entry = Site(url = url)
            self._db.session.add(site_entry)
            self._db.session.commit()
        return site_entry
    
    def  get_site_by_url(self, url):
        try:
            return self._db.session.query(Site).filter(Site.url == url).one_or_none()
        except:
            return None

    def get_site_by_id(self, site_id):
        try:
            return self._db.session.query(Site).get(site_id)
        except:
            return None
