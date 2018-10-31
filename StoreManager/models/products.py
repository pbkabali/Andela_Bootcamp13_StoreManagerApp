import psycopg2
from ..db.db import DbConnection
from flask import request


class Product(DbConnection):
    
    
    def add_a_product(self, name, unit, unit_price, quantity, minimum_quantity,category):        
        command = """INSERT INTO products (product_name, unit,
            unit_price, quantity, minimum_quantity, category) VALUES ( %s, %s, %s,%s, %s,%s) """
        self.cursor.execute(
            command, (name, unit, unit_price, quantity, minimum_quantity,category)                         
        )       
       
    def get_products(self):
        command = """SELECT * FROM products"""
        self.cursor.execute(command)
        products = self.cursor.fetchall()
        return products    

    def duplicate_product(self, product_name):
        command = """SELECT * FROM products WHERE product_name = %s"""
        self.cursor.execute(command, product_name)
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False  

if __name__=="__main__":
    product = Product()  
    for i in product.get_products():
        print (i)


    
        
        
        
        

      