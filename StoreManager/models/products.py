import psycopg2
from ..db.db import DbConnection


class Product(DbConnection):
    
    
    def addProduct(self, name, unit, unit_price, quantity, minimum_quantity,category):        
        command = """INSERT INTO products (product_name, unit,
            unit_price, quantity, minimum_quantity, category) VALUES ( %s, %s, %s,%s, %s,%s) """
        self.cursor.execute(
            command, (name, unit, unit_price, quantity, minimum_quantity,category)                         
        )       
       
    def duplicateProduct(self, name):
        command = """SELECT * FROM products WHERE product_name = %s"""
        self.cursor.execute(command, [name])
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

    def getProducts(self):
        command = """SELECT * FROM products"""
        self.cursor.execute(command)
        products = self.cursor.fetchall()
        return products  

    def getProductbyId(self, productId):
        command = """SELECT * FROM products WHERE id = %s"""   
        self.cursor.execute(command,[productId])
        return self.cursor.fetchone()






if __name__=="__main__":
    product = Product()  
    for i in product.get_products():
        print (i)


    
        
        
        
        

      