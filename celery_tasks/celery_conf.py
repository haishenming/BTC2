'''
Created on 2017年12月04日 下午6:00

@author: xiangyufan@juwang.cn

读取配置文件
'''
from datetime import timedelta

from celery import Celery

def init_conf(env="dev"):
    """ 初始化配置
    """

    my_celery = Celery("main_tasks", backend='redis://localhost',
             broker='redis://localhost')

    my_celery.config_from_object('config.setting_{}'.format(env))

    my_celery.conf.update(
        CELERY_TIMEZONE='UTC',
        CELERY_ACCEPT_CONTENT=['json'],
        CELERY_TASK_SERIALIZER='json',
        CELERY_RESULT_SERIALIZER='json',

        # 定时执行器
        CELERYBEAT_SCHEDULE={
            # 30秒心跳
            'get_future_broker': {
                'task': 'tasks.get_future_broker',
                'schedule': timedelta(seconds=5),
            },
            'get_future_index': {
                'task': 'tasks.get_future_index',
                'schedule': timedelta(seconds=10),
            },
            'create_excel': {
                'task': 'tasks.create_excel',
                'schedule': timedelta(days=1),
            }
        }
    )

    return my_celery

