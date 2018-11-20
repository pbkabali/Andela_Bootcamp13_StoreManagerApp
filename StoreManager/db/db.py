import psycopg2
from psycopg2.extras import RealDictCursor
from .. import app
from .. import config


class DbConnection:

    def __init__(self):

        if app.config.get('ENV') == 'development':
            dbname = config.DevelopmentConfig.DATABASE
            host = config.DevelopmentConfig.HOST
            user = config.DevelopmentConfig.USER
            password = config.DevelopmentConfig.PASSWORD

        if app.config.get('ENV') == 'testing':
            dbname = config.TestingConfig.DATABASE
            host = config.TestingConfig.HOST
            user = config.TestingConfig.USER
            password = config.TestingConfig.PASSWORD

        if app.config.get('ENV') == 'production':
            dbname = config.ProductionConfig.DATABASE
            host = config.ProductionConfig.HOST
            user = config.ProductionConfig.USER
            password = config.ProductionConfig.PASSWORD

        try:
            self.connect = psycopg2.connect(dbname = dbname, user = user,
             host = host, password = password, port=5432, cursor_factory=RealDictCursor)
            print('Database succesfully connected')
        except Exception as e:
            print(e)
            print('failed to connect database!')    
        self.cursor = self.connect.cursor()
        self.connect.autocommit = True    

    def create_db_tables(self):  
        
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
            users_id SMALLSERIAL PRIMARY KEY
            ,first_name VARCHAR(50) NOT NULL
            ,last_name VARCHAR(50)
            ,username VARCHAR(10) UNIQUE NOT NULL
            ,password VARCHAR NOT NULL
            ,role VARCHAR(5) NOT NULL
            ,created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
            )            
            """,
            """
            CREATE TABLE IF NOT EXISTS products(
            product_id SERIAL PRIMARY KEY
            ,product_name VARCHAR(50) NOT NULL
            ,unit VARCHAR(10) NOT NULL
            ,unit_price INT NOT NULL
            ,quantity SMALLINT NOT NULL
            ,minimum_quantity SMALLINT 
            ,category VARCHAR(30)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sales(
            sale_id SMALLSERIAL PRIMARY KEY
            ,attendant_id SMALLINT REFERENCES users(users_id)
            ,product_id SMALLINT NOT NULL            
            ,quantity SMALLINT NOT NULL           
            ,total_price INT NOT NULL
            ,created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        for i in commands:
            self.cursor.execute(i)

    
        

if __name__=="__main__":
    db = DbConnection()
    
   
    
            
          


        