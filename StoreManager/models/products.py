import psycopg2
from ..db.db import DbConnection


class Product(DbConnection):
    
    
    def addProduct(self, name, unit, unit_price, quantity, minimum_quantity,category):        
        command = """INSERT INTO products (product_name, unit,
            unit_price, quantity, minimum_quantity, category) VALUES ( %s, %s, %s,%s, %s,%s) """
        self.cursor.execute(
            command, (name, unit, unit_price, quantity, minimum_quantity,category)                         
        )      
        return {
            "product_name": name,
            "unit_price" : unit_price,
            "initial_quantity": quantity,
            "minimum_quantity": minimum_quantity
            } 
       
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
        command = """SELECT * FROM products WHERE product_id = %s"""   
        self.cursor.execute(command,[productId])
        return self.cursor.fetchone()

    def modifyProduct(self, productId, characteristic, value):
        command = """UPDATE products SET %s = %s WHERE product_id = %s """    
        self.cursor.execute(command, (characteristic, value, productId))
       

    def deleteProduct(self, productId):
        command = """DELETE * FROM products WHERE product_id = %s"""
        self.cursor.execute(command,[productId])
    



if __name__=="__main__":
    product = Product()  
    for i in product.getProducts():
        print (i)


    
        
        
        
        

      