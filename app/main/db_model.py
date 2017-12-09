
from ..models import Okex, OkexPlus


def get_new_okexs_by_symbol(symbol, num=5):
    """ 获取最新的okex数据,可设置数量
    """

    return Okex.query.filter_by(symbol=symbol).order_by(
        Okex.create_time.desc(

    )).limit(num).all()

def get_new_okex_plus(num=5):
    """ 获取最新的okex统计数据
    """
    return OkexPlus.query.filter_by().order_by(
        OkexPlus.create_time.desc(
        )).limit(num).all()

