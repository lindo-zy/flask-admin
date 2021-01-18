#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Config(object):
    DEBUG = True
    REDIS_HOST = '127.0.0.1'


class DevelopmentConfig(Config):
    DEBUG = True
    # redis配置
    REDIS_HOST = '0.0.0.0'
    REDIS_PORT = 6379

    # 日志配置


class ProductionConfig(Config):
    DEBUG = False


project_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
