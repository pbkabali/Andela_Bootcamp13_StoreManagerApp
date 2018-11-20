class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'   
    TESTING = False
    JWT_SECRET_KEY = 'jwt-secret'
    DATABASE = 'store'
    HOST = "localhost"    
    USER = "postgres"
    PASSWORD = "polos241!"
    PORT = 5432

class TestingConfig(BaseConfig):
    DEBUG = True
    ENV = 'testing'    
    TESTING = True
    JWT_SECRET_KEY = 'jwt-secret'
    DATABASE = 'test_db'
    HOST = ""    
    USER = ""
    PASSWORD = ""

class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    TESTING = False
    JWT_SECRET_KEY = 'jwt-secret'
    DATABASE = "d8sbh9eskd95ro"
    HOST = "ec2-54-83-8-246.compute-1.amazonaws.com"    
    USER = "cknasryycxsqrp"
    PASSWORD = "26290e4ddea5a6d6fad04f3b060c75c4780ab517e9c613cff6dfeb6046bd507a"
    