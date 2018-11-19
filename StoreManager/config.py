class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    DATABASE = 'store'
    TESTING = False
    JWT_SECRET_KEY = 'jwt-secret'

class TestingConfig(BaseConfig):
    DEBUG = True
    ENV = 'testing'
    DATABASE = 'test_db'
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    TESTING = False
    