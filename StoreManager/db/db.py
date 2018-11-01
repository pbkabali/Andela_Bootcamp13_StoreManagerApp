import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app, g


class DbConnection:

    def __init__(self):
        try:
            self.connect = psycopg2.connect(dbname="store", user="postgres",
             host="localhost", password = "polos241!",port=5432, cursor_factory=RealDictCursor)#
            print('Database STORE succesfully connected')
        except Exception as e:
            print(e)
            print('failed to connect')    
        self.cursor = self.connect.cursor()
        self.connect.autocommit = True
        # except Exception as e:
        #     print (e)
        #     print ("failed to connect db")    


#         #     self.g = g   			
            

#     # def get_db(self):
#     #     if "db" not in g:
#     #         self.g.db = psycopg2.connect(current_app.config['DATABASE']) 
#     #     return self.g.db      

    # def close_db(self):
    #     self.db = g.po('db')
    #     if self.db is not None:
    #         self.db.close()

    def create_db_tables(self):  
        # self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INT, username VARCHAR)""")
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
            id SMALLSERIAL PRIMARY KEY
            ,first_name VARCHAR(50) NOT NULL
            ,last_name VARCHAR(50)
            ,username VARCHAR(10) UNIQUE NOT NULL
            ,created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
            )            
            """,
            """
            CREATE TABLE IF NOT EXISTS products(
            id SERIAL PRIMARY KEY
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
            id SMALLSERIAL PRIMARY KEY
            ,attendant_id SMALLINT REFERENCES users(id)
            ,product_id SMALLINT REFERENCES products(id)            
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
    
   
    
            
          


        