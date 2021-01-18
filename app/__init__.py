#!/usr/bin/python3
# -*- coding:utf-8 -*-
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config)

    # 设置主页
    @app.route('/')
    def index():
        return '服务启动成功！'

    # 注册蓝图

    return app
