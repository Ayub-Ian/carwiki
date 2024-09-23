class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgrespw@localhost:5432/carwiki'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
