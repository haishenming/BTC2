'''
Created on 2017年12月05日 下午12:41

@author: xiangyufan@juwang.cn

'''



def merge_record(instance):
    """ 存在则修改，不存在则插入, 要求传入的是 models中的类
    """
    session.merge(instance)
    session.commit()
    return instance


def get_obex():
    """ 获取obex数据
    """