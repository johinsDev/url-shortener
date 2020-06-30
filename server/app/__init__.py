from flask import Flask
from .models import db
from .models.link import Link
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)

migrate = Migrate(app, db)


def create_app(env):
    app.config.from_object(env)

    if not database_exists(env.SQLALCHEMY_DATABASE_URI):
        create_database(env.SQLALCHEMY_DATABASE_URI)

    with app.app_context():
        db.init_app(app)

    return app
