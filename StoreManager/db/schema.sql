CREATE TABLE IF NOT EXISTS products(
    product_id SMALLSERIAL PRIMARY KEY
    ,first_name VARCHAR(50) NOT NULL
    ,last_name VARCHAR(50)
    ,username VARCHAR(10) UNIQUE NOT NULL
    ,password VARCHAR(50) NOT NULL
    ,role VARCHAR(5) NOT NULL
    ,created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP                  
);

CREATE TABLE IF NOT EXISTS users(
    users_id SERIAL PRIMARY KEY
    ,product_name VARCHAR(50) NOT NULL
    ,unit VARCHAR(10) NOT NULL
    ,unit_price INT NOT NULL
    ,quantity SMALLINT NOT NULL
    ,minimum_quantity SMALLINT 
    ,category VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS sales(
    sale_sid SMALLSERIAL PRIMARY KEY
    ,attendant_id SMALLINT REFERENCES users(users_id)
    ,product_id SMALLINT REFERENCES products(product_id)            
    ,quantity SMALLINT NOT NULL           
    ,total_price INT NOT NULL
    ,created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);