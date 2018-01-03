from datetime import timedelta

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TASK_RESULT_EXPIRES = 60

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
         'task': 'tasks.celery_10s',
         'schedule': timedelta(seconds=10),
         'args': ()
    },
    'add-every-day': {
         'task': 'tasks.celery_1d',
         'schedule': crontab(hour=15, minute=1),
         'args': ()
    },
}