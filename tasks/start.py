'''
Created on 2017年12月06日 下午2:23

@author: xiangyufan@juwang.cn

定时任务核心代码

'''

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks_func import add_ticker

def tasks():
    add_ticker()

sched = BlockingScheduler()
sched.add_job(tasks, 'interval', seconds=60)
sched.start()

