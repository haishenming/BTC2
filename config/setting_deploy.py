'''
Created on 2017年11月30日 下午3:06

@author: xiangyufan@juwang.cn

'''

#################### API url #####################
# 获取OKEX合约行情
FUTURE_TICKER_URL = 'https://www.okex.com/api/v1/future_ticker.do'

# 获取OKEX合约指数信息
FUTURE_INDEX_URL = 'https://www.okex.com/api/v1/future_index.do'


# celery 中间件
CELERY_BROKER = 'redis://localhost'
# celery backend
CELERY_BACKEND = 'redis://localhost'