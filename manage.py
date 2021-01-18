#!/usr/bin/python3
# -*- coding:utf-8 -*-
from flask_script import Manager

from app import create_app
from config import project_config

app = create_app(project_config['development'])

manager = Manager(app)


@manager.command
def start():
    print('启动服务')


if __name__ == '__main__':
    manager.run()
