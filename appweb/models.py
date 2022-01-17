from appweb import mongo
from datetime import datetime


class Account(mongo.Document):
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
