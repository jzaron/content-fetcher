"""
@author: jzaron
"""

# TODO: refresh content
# TODO: errors handling

from fetcher import db, storage, app
from fetcher.db_actions import DbActions
import sys
import uuid

TASK_CATEGORY_SCRAP_TEXT = 'scrap_text'
TASK_CATEGORY_SCRAP_IMAGES = 'scrap_images'

dbactions = DbActions(db)


def scrap_text(site):
    try:
        site_entry = dbactions.get_or_put_site(site)
        if not dbactions.get_task_by_site_and_category(
                site_entry, TASK_CATEGORY_SCRAP_TEXT):
            job_id = str(uuid.uuid4())
            dbactions.put_task(site_entry, job_id, TASK_CATEGORY_SCRAP_TEXT)
            job = app.task_queue.create_job('fetcher.tasks.scrap_text', (site_entry.id, get_text_path(site_entry.id)),
                                            job_id=job_id)
            app.task_queue.enqueue_job(job)
            return job_id
    except BaseException as e:
        print(type(e), file=sys.stderr)
        print(e, file=sys.stderr)
        return None


def get_text(text_id):
    text_entry = dbactions.get_text_by_id(text_id)
    if text_entry:
        return storage.get_text(get_text_path(text_entry.site_id))


def get_text_path(site_id):
    return f'{site_id}/text'


def scrap_images(site):
    try:
        site_entry = dbactions.get_or_put_site(site)
        if not dbactions.get_task_by_site_and_category(
                site_entry, TASK_CATEGORY_SCRAP_IMAGES):
            job_id = str(uuid.uuid4())
            dbactions.put_task(site_entry, job_id, TASK_CATEGORY_SCRAP_IMAGES)
            job = app.task_queue.create_job('fetcher.tasks.scrap_images', (site_entry.id, get_image_path),
                                            job_id=job_id)
            app.task_queue.enqueue_job(job)
            return job_id
    except BaseException as e:
        print(type(e), file=sys.stderr)
        print(e, file=sys.stderr)


def get_image(image_id):
    image_entry = dbactions.get_image_by_id(image_id)
    if image_entry:
        return storage.get_image(get_image_path(image_entry.site_id, image_entry.id))


def get_image_path(site_id, image_id):
    return f'{site_id}/{image_id}'


def get_task(task_id):
    return dbactions.get_task_by_id(task_id)


def get_site(site_id):
    return dbactions.get_site_by_id(site_id)
