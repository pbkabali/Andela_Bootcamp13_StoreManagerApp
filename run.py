
from StoreManager import create_app
from StoreManager.db.db import DbConnection

app = create_app()
ENV = 'development'
db = DbConnection()


if __name__ == '__main__':
    app.run(debug=True)
    db.create_db_tables()

