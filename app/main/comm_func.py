
from manage import app


def parse_okex_data(okexs):
    """ 解析数据
    """
    pass


def get_symbol_dic_config():
    """ 从配置文件中获取symbol字典
    """
    symbol_dic = app.config.get("symbol_dic".upper())

    return symbol_dic