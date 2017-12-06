'''
Created on 2017年12月06日 下午2:25

@author: xiangyufan@juwang.cn

'''

from tasks_data.db_models import Okex
from tasks_data.db_config import DBSession


def merge_record(instance):
    """ 存在则修改，不存在则插入, 要求传入的是 models中的类
    """
    session = DBSession()
    session.merge(instance)
    session.commit()
    return instance