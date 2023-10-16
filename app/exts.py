
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_restful import Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_redis import FlaskRedis
# 初始化
db = SQLAlchemy()
rd = FlaskRedis()
migrate = Migrate()
cache = Cache(config={
    'CACHE_TYPE': 'simple'  # 缓存类型
})  # 装饰器装饰视图@cache.cached(timeout=20) cache.get(key) cache.set(key,'a',timeout=1)
api = Api()
limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)


# 和app绑定 在__init__.py调用init_exts
def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app)
    api.init_app(app=app)
    limiter.init_app(app=app)
    rd.init_app(app=app)