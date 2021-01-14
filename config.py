#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Config(object):
    DEBUG = True

    REDIS_HOST = '127.0.0.1'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
