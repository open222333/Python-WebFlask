import os
from datetime import timedelta
from pymongo.read_preferences import ReadPreference
from celery.schedules import crontab


class BaseConfig:
    # 基本配置
    # https://dormousehole.readthedocs.io/en/latest/config.html
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', None)
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)

    # mongodb
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGO_HOST', '127.0.0.1:27017'),
        'username': os.environ.get('MONGO_HOST_USERNAME', None),
        'password': os.environ.get('MONGO_HOST_PASSWORD', None),
        # 時區 依照文檔的值回傳時區
        'tz_awrae': True
    }
    if len(os.environ.get('MONGO_REPLICA_SET', '')) > 0:
        # 若有集群設定
        MONGODB_SETTINGS['replicaSet'] = os.environ.get('MONGO_REPLICA_SET', '')
        # https://docs.mongodb.com/manual/core/read-preference/
        MONGODB_SETTINGS['read_preference'] = ReadPreference.NEAREST

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_BINDS = {
        'sqlalchemyA': os.environ.get('SQLALCHEMY_A_DATABASE_URI'),
        'sqlalchemyB': os.environ.get('SQLALCHEMY_B_DATABASE_URI')
    }
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 250,
        'max_overflow': 50,
        'pool_size': 500,
        'pool_pre_ping': True,
        'pool_use_lifo': True,
    }

    # celery
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    CELERY_ENABLE_UTC = os.environ.get('CELERY_ENABLE_UTC', True)
    CELERY_TIMEZONE = os.environ.get('CELERY_TIMEZONE', 'utc')
    CELERY_ACCEPT_CONTENT = os.environ.get('CELERY_ACCEPT_CONTENT', ['msgpack'])
    CELERY_TASK_SERIALIZER = os.environ.get('CELERY_TASK_SERIALIZER', 'msgpack')
    CELERY_RESULT_SERIALIZER = os.environ.get('CELERY_RESULT_SERIALIZER', 'msgpack')
    CELERY_MESSAGE_COMPRESSION = os.environ.get('CELERY_MESSAGE_COMPRESSION', 'bzip2')
    CELERY_ALWAYS_EAGER = os.environ.get('CELERY_ALWAYS_EAGER', False)

    CELERYBEAT_SCHEDULE = {}
    if os.environ.get('CELERT_1'):
        # 加入排程
        CELERYBEAT_SCHEDULE[''] = {
            'task': '',
            'schedule': crontab(minute='*')
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
