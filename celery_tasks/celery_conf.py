'''
Created on 2017年12月04日 下午6:00

@author: xiangyufan@juwang.cn

读取配置文件
'''

from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config[
        'CELERY_BROKER'], backend=app.config[
        'CELERY_BACKEND'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

