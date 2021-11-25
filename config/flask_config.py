import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__name__))


class BaseConfig:
    # 基本配置
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)
    MONGODB_SETTINGS = {
        'host': os.environ.get(''),
        'username': os.environ.get('', None),
        'password': os.environ.get('', None),
        # 時區 依照文檔的值回傳時區
        'tz_awrae': True
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
