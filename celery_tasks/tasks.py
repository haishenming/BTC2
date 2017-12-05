'''
Created on 2017年12月04日 下午6:01

@author: xiangyufan@juwang.cn

任务信息
'''

from celery_tasks.celery_conf import init_conf
# from celery_tasks.database.models import Okex
# from celery_tasks.database.db_func import merge_record


my_celery = init_conf()

@my_celery.task
def get_future_broker():
    """ 获取future_broker 每分钟运行一次
    """
    with open("jk.txt", "a", encoding="utf-8") as f:
        f.write("jdksajf")

@my_celery.task
def get_future_index():
    """ 获取future_index 每分钟运行一次
    """
    pass


@my_celery.task
def create_excel():
    """ 生成excel文件 每天运行一次
    """
    pass






