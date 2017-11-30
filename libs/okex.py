'''
Created on 2017年11月30日 下午2:59

@author: xiangyufan@juwang.cn

'''

import requests
from setting import future_index_url, future_ticker_url

class OKEX:
    """ 获取和操作BTC数据
    """

    def __init__(self, symbol):
        self.symbol = symbol

    def get_future_index(self):
        """
        :return: 获取OKEX合约指数信息
        """
        data = {
            "symbol": self.symbol
        }

        response = requests.get(future_index_url, params=data)

        if response.status_code == requests.codes.ok:
            rdata = response.json()

            if rdata.get('error_code'):
                return {}, rdata
            else:
                return rdata, {'result': True, 'error_code': 0}
        else:
            return {}, {'result': False, 'error_code': response.status_code}


if __name__ == '__main__':
    btc = OKEX(symbol='btcusd')
    btc.get_future_index()