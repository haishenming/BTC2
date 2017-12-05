'''
Created on 2017年12月05日 下午12:41

@author: xiangyufan@juwang.cn

'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tasks import my_celery


engine = create_engine(my_celery.config["DB_URL"], echo=my_celery.config["DB_ECHO"],
                       convert_unicode=True)

DB_Session = sessionmaker(bind=engine)
session = DB_Session()