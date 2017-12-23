from datetime import datetime
import os

from app import create_app, db
from app.models import Okex
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


# shell启动配置
def make_shell_context():
    return dict(app=app, db=db, Okex=Okex)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('dev')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
