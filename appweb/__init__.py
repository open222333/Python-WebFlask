from re import template
from flask import Flask, config
from flask_mongoengine import MongoEngine


mongo = MongoEngine()


def create_app(config_name=None):
    app = Flask(__name__, static_folder='static')
    # app.config.from_object(config[config_name])
    mongo.init_app(app)

    # 每個藍圖可以有自己的 模板 靜態目錄 視圖 URL規則
    from appweb.v01.view import app_v01
    app.register_blueprint(app_v01, url_prefix='/v01')

    return app
