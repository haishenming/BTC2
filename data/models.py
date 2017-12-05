'''
Created on 2017年12月05日 下午12:41

@author: xiangyufan@juwang.cn

'''


from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Okex(Base):
    __tablename__ = "okex"

