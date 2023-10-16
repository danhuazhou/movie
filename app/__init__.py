import os
import datetime
from flask import Flask, render_template
from .exts import init_exts
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
# from . import home
import os

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:dan.987@192.168.25.10:3306/movie"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# app.config["SECRET_KEY"] = "2751803d969c4e7ab2294cdbe72654c3"
# app.config["UP_DIR"] = '/mnt/sd/files/movies'
# app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
# app.config["REDIS_URL"] = "redis://127.0.0.1:6379/0"
#
# app.debug = True
# db = SQLAlchemy(app)
# rd = FlaskRedis(app)
#
from app.home.views import home as home_bluepprint
from app.admin.views import admin as admin_blueprint
#
# app.register_blueprint(home_bluepprint)
# app.register_blueprint(admin_blueprint, url_prefix="/admin")

def create_app():
    static_folder = 'static'
    # static_folder = os.path.join(BASE_DIR, 'static')
    template_folder = 'templates'
    app = Flask(__name__, static_folder=static_folder,
                template_folder=template_folder)

    # 注册view中的蓝图
    app.register_blueprint(blueprint=home_bluepprint)
    app.register_blueprint(blueprint=admin_blueprint, url_prefix="/admin")

    # session配置 使用session需要配置SECRET_KEY
    # print(app.config)
    # app.config['DEBUG'] = False
    app.config['SECRET_KEY'] = '123test'
    app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=7)

    # 配置数据库
    # db_uri = 'sqlite:///sqlite3.db'
    HOSTNAME = "192.168.25.10"
    PORT = 3306
    USERNAME = "root"
    PASSWORD = "dan.987"
    DATABASE = "movie"
    db_uri = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁止对象追踪修改

    app.config["UP_DIR"] = '/mnt/sd/files/movies'
    app.config["FC_DIR"] = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
    app.config["REDIS_URL"] = "redis://127.0.0.1:6379/0"

    # 初始化插件
    init_exts(app=app)

    return app

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("home/404.html"), 404
