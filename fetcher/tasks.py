"""
@author: jzaron
"""

from rq import get_current_job

from fetcher import db, scraper, storage
from fetcher.db_actions import DbActions


# TODO: THIS IS TO REWORK
# TODO: The approach should be reworked to avoid any db actions in RQ tasks. In case of need to signalize a task
# has finished, a HTTP request should be sent to the application using dedicated REST API endpoint, so only the
# application will handle database operations.


def scrap_text(site_id, storage_path):
    dbactions = DbActions(db)
    job = get_current_job()
    task = dbactions.get_task_by_id(job.get_id())
    site_entry = dbactions.get_site_by_id(site_id)
    text = scraper.get_text(site_entry.url)
    storage.put_text(text, storage_path)
    dbactions.put_text(site_entry)
    job.meta['progress'] = '1/1'
    job.save_meta()
    task.finished = True
    db.session.commit()


def scrap_images(site_id, storage_path_func):
    dbactions = DbActions(db)
    job = get_current_job()
    task = dbactions.get_task_by_id(job.get_id())
    site_entry = dbactions.get_site_by_id(site_id)
    urls = scraper.get_image_urls(site_entry.url)
    n = 0
    for url in urls:
        image_entry = dbactions.put_image(site_entry, url)
        storage.put_image(url, storage_path_func(site_entry.id, image_entry.id))
        db.session.commit()
        n += 1
        job.meta['progress'] = f'{n}/{len(urls)}'
        job.save_meta()
    task.finished = True
    db.session.commit()
