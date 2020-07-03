from flask import Flask
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists, create_database
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})

migrate = Migrate(app, db)


def create_app(env):
    app.config.from_object(env)

    if not database_exists(env.SQLALCHEMY_DATABASE_URI):
        create_database(env.SQLALCHEMY_DATABASE_URI)

    with app.app_context():
        db.init_app(app)
        cache.init_app(app)

    return app
