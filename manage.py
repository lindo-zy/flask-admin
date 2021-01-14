#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask_script import Manager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

manager = Manager(app)


@manager.command
def start():
    print('启动服务')


if __name__ == '__main__':
    manager.run()
