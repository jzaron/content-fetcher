"""
@author: jzaron
"""

from fetcher import db
from flask import current_app
import redis
import rq


class Site(db.Model):
    __tablename__ = 'Site'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512), index=True, unique=True)
    text = db.relationship('Text', backref='site', lazy=True)
    images = db.relationship('Image', backref='site', lazy=True)
    tasks = db.relationship('Task', backref='site', lazy='dynamic')

    def __repr__(self):
        return f'<Site {self.url}>'

    def launch_task(self, name, description, *args, **kwargs):
        rq_job = current_app.task_queue.enqueue('app.tasks.' + name, self.id,
                                                *args, **kwargs)
        task = Task(id=rq_job.get_id(), name=name, description=description,
                    user=self)
        db.session.add(task)
        return task

    def get_tasks_in_progress(self):
        return Task.query.filter_by(site=self, complete=False).all()

    def get_task_in_progress(self, name):
        return Task.query.filter_by(name=name, user=self,
                                    complete=False).first()


class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.String(36), primary_key=True)
    category = db.Column(db.String(32), index=True)
    finished = db.Column(db.Boolean, default=False)
    site_id = db.Column(db.Integer, db.ForeignKey('Site.id'))

    def __repr__(self):
        return f'<Task category:{self.category} finished:{self.finished}' \
            f' site_id:{self.site_id}>'

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(self.id, connection=current_app.redis)
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', '-') if job is not None else 'finished'
