'''
Created on 2017年12月04日 下午2:23

@author: xiangyufan@juwang.cn

'''
import time
from celery_tasks import add, add2


ret1 = add.delay(1, 2)
# time.sleep(2)
ret2 = add2.delay(1, 3)

time.sleep(1)

print(ret1.ready())
print(ret2.ready())

print(ret1.get())
print(ret2.get())



print(100)