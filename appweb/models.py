from appweb import mongo, sqlalchemy
from datetime import datetime


class Account(mongo.Document):
    # https://docs.mongoengine.org/guide/defining-documents.html
    account = mongo.StringField(required=True)
    password = mongo.StringField(required=True)
    create_date = mongo.DateTimeField()
    modified_date = mongo.DateTimeField(default=datetime.now())

    meta = {
        'indexes': ['account']
    }

    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        return super(Account, self).save(*args, **kwargs)


class User(sqlalchemy.Model):
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types
    # __bind_key__ = '' 使用哪個資料庫
    uid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(80), unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(80))

