from __future__ import absolute_import
from celery import Celery

app = Celery('celery_tasks', include=['tasks'])

app.config_from_object('config')

if __name__ == '__main__':
    app.start()
