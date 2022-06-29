from flask import Flask 
from .extensions import db, migrate
from .config import Config


def creat_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)

    return app