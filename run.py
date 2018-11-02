
from StoreManager import create_app
from StoreManager.db.db import DbConnection
from StoreManager import config

app = create_app(config.DevelopmentConfig)

db = DbConnection()


if __name__ == '__main__':
    app.run()
    db.create_db_tables()

