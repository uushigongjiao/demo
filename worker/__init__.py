import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

celery_app = Celery('demo')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()


def call_by_worker(func):
    task = celery_app.task(func)
    return task.delay