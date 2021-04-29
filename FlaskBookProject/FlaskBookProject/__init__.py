from flask import Flask
from .extensions import mongo
from .books import bp


def create_app(config_object='FlaskBookProject.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)

    app.register_blueprint(bp)

    return app
