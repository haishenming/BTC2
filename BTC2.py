from flask import Flask
from flask import render_template

app = Flask(__name__)

# 导入配置
app.config.from_object('config.setting')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
