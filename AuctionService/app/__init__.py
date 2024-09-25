from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from services.contract import ExchangeManager

db = SQLAlchemy()
migrate = Migrate()
manager = ExchangeManager()

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Load config from single file

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.auction import routes
    app.register_blueprint(routes, url_prefix='/api')

    manager.declare_exchange('AuctionSvc.AuctionCreated', 'fanout')
    return app
