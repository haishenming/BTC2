'''
Created on 2017年12月04日 下午2:21

@author: xiangyufan@juwang.cn

'''
import time
from celery import Celery

app = Celery('tasks', backend='redis://localhost',
             broker='redis://localhost')

@app.task
def add(x, y):
    time.sleep(2)
    return x + y

@app.task
def add2(x, y):
    return x + y