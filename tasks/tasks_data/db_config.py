'''
Created on 2017年12月06日 下午2:24

@author: xiangyufan@juwang.cn

数据库配置
'''
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = "sqlite:///./data.db"
DB_ECHO = True

# 初始化数据库连接:
engine = create_engine(DB_URL, echo=DB_ECHO)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


