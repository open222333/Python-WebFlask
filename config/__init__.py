from flask import Flask, config
from flask_mongoengine import MongoEngine


mongo = MongoEngine()


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    mongo.init_app(app)

    return app
