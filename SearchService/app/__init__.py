from flask import Flask
from flask_pymongo import PyMongo

pymongo = PyMongo()
def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Load config from single file
    pymongo.init_app(app)
    from app.routes.search import routes
    app.register_blueprint(routes, url_prefix='/api')
    return app
