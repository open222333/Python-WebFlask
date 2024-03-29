from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from config.flask_config import config
from appweb.v01.view import app_v01
import os


mongo = MongoEngine()
sqlalchemy = SQLAlchemy()


def create_app(config_name=None):
    # 基本Flask設定
    app = Flask(
        __name__,
        static_folder='../static',
        template_folder='../templates'
    )

    @app.route("/")
    def web_status():
        return 'ok'

    # 載入設定檔
    if config_name != None:
        app.config.from_project(config[config_name])

    # init_app用於控制一個包與一個或多個Flask應用程序的集成
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy.init_app
    if os.environ.get("MONGO_HOST", None) != None:
        mongo.init_app(app)
    if os.environ.get("SQLALCHEMY_DATABASE_URI", None) != None:
        sqlalchemy.init_app(app)

    # 每個藍圖可以有自己的 模板 靜態目錄 視圖 URL規則
    app.register_blueprint(app_v01, url_prefix='/v01')

    return app
