'''
Created on 2017年12月05日 下午3:53

@author: xiangyufan@juwang.cn

'''

from flask import render_template

from core import app


@app.route('/')
def index():
    render_template('index.html')