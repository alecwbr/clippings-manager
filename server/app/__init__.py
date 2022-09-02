from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from app.apiv1 import api as apiv1_bp
    app.register_blueprint(apiv1_bp, url_prefix='/api/v1')

    return app