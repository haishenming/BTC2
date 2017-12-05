'''
Created on 2017年12月04日 下午6:00

@author: xiangyufan@juwang.cn

读取配置文件
'''

from celery import Celery

def init_conf(env="dev"):
    """ 初始化配置
    """

    my_celery = Celery("main_tasks", backend='redis://localhost',
             broker='redis://localhost')

    my_celery.config_from_object('config.setting_{}'.format(env))

    return my_celery

