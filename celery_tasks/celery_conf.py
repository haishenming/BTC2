'''
Created on 2017年12月04日 下午6:00

@author: xiangyufan@juwang.cn

读取配置文件
'''

from celery import Celery

def init_conf(app):
    """ 初始化配置
    """

    my_celery = Celery("main_tasks", backend=app.config["CELERY_BROKER"],
             broker=app.config["CELERY_BROKER"])

    my_celery.conf.update(app.config)

    return my_celery

