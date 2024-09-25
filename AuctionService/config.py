class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgrespw@localhost:5432/carwiki'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = '127.0.0.1:7001'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
