'''
Created on 2017年12月05日 下午3:51

@author: xiangyufan@juwang.cn

核心代码
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from celery_tasks.celery_conf import init_conf

from flask import Flask

app = Flask(__name__)

my_celery = init_conf(app)

engine = create_engine(app.config["DB_URL"], echo=app.config["DB_ECHO"],
                       convert_unicode=True)

DB_Session = sessionmaker(bind=engine)
session = DB_Session()