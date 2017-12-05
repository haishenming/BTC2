'''
Created on 2017年12月04日 下午6:01

@author: xiangyufan@juwang.cn

任务信息
'''

from celery_tasks.celery_conf import init_conf


my_celery = init_conf()


@my_celery.task()
def get_future_broker():
    """ 获取future_broker
    """
    pass

@my_celery.task()
def get_future_index():
    """ 获取future_index
    """

@my_celery.task()
def create_excel():
    """ 生成excel文件
    """
    pass






