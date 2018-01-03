'''
Created on 2017年11月30日 下午4:02

@author: xiangyufan@juwang.cn

'''

import requests
import time

print("正在生成字典")
test_dic = {str(k):v for k in range(10000) for v in range(10000)}

start1 = time.time()
for k, v in test_dic.items():
    pass
end1 = time.time() - start1
print("end1:", end1)


start2 = time.time()
for k, v in test_dic.items():
    pass
end2 = time.time() - start2
print("end2", end2)