class Config:
    MONGO_URI = 'mongodb://root:mongopw@localhost:27017/SearchDb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
