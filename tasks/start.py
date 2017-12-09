'''
Created on 2017年12月06日 下午2:23

@author: xiangyufan@juwang.cn

定时任务核心代码

'''

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks_func import add_ticker

def task_60s():
    """ 一分钟一次
    """
    add_ticker()

def task_1d():
    """ 一天一次
    """


sched = BlockingScheduler()
sched.add_job(task_60s, 'interval', seconds=60)
sched.start()

