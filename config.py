"""
配置文件
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 'P4gZdDz6n2KM7QM2x2pt9sq87MBuaQTqSc99GQmU'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    # FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') @ staticmethod

    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True
    # 未使用邮件功能
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir + '/tasks',
                                                          'data.db')
    print(SQLALCHEMY_DATABASE_URI)



config = {'development': DevelopmentConfig,
          'default': DevelopmentConfig
          }
