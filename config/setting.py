'''
Created on 2017年12月05日 下午12:42

@author: xiangyufan@juwang.cn

开发配置
'''

#################### API url #####################
# 获取OKEX合约行情
FUTURE_TICKER_URL = 'https://www.okex.com/api/v1/future_ticker.do'

# 获取OKEX合约指数信息
FUTURE_INDEX_URL = 'https://www.okex.com/api/v1/future_index.do'


################### celery ###################
# celery 中间件
CELERY_BROKER = 'redis://localhost'
# celery backend
CELERY_BACKEND = 'redis://localhost'



################ database ##################
DB_URL = "sqlite:///data/data.db"
DB_ECHO = True