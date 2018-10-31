CREATE TABLE IF NOT EXISTS users (
    id SMALLSERIAL PRIMARY KEY
    ,first_name VARCHAR(50) NOT NULL
    ,last_name VARCHAR(50)
    ,username VARCHAR(10) UNIQUE NOT NULL
    ,created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY
    ,product_name VARCHAR(50) NOT NULL
    ,unit VARCHAR(10) NOT NULL
    ,unit_price NUMERIC NOT NULL
    ,quantity SMALLINT NOT NULL
    ,minimum_quantity SMALLINT 
    ,category VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS sales(
    id SMALLSERIAL PRIMARY KEY
    ,attendant_id SMALLINT REFERENCES users(id)
    ,product_id VARCHAR(50) REFERENCES products(id)
    ,quantity SMALLINT NOT NULL
    ,unit_price NUMERIC REFERENCES products(unit_price)
    ,total_price NUMERIC NOT NULL
    ,created_at TIMESTAMPTZ
);