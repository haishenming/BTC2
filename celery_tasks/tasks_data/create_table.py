'''
Created on 2017年12月06日 下午3:15

@author: xiangyufan@juwang.cn

'''
from sqlalchemy import MetaData

from tasks_data.db_config import DBSession, engine

metadata = MetaData(engine)
metadata.create_all(engine)