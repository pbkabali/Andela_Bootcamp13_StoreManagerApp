from StoreManager import app
from StoreManager.db.db import DbConnection

db = DbConnection()
db.create_db_tables()

if __name__ == '__main__':
    app.run()
   

