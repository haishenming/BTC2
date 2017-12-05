from core import app

# 导入配置
def init_conf(env="dev"):
    """ 初始化配置
    """
    app.config.from_object('config.setting_{}'.format(env))





if __name__ == '__main__':
    init_conf()
    app.run()
