'''
Created on 2017年12月05日 下午3:51

@author: xiangyufan@juwang.cn

核心代码
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from celery_tasks.celery_conf import make_celery

from flask import Flask

app = Flask(__name__)

def init_conf(env="dev"):
    """ 初始化配置
    """
    app.config.from_object('config.setting_{}'.format(env))

init_conf("dev")

celery = make_celery(app)

engine = create_engine(app.config["DB_URL"], echo=app.config["DB_ECHO"],
                       convert_unicode=True)

DB_Session = sessionmaker(bind=engine)
session = DB_Session()