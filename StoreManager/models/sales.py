
import psycopg2
from ..db.db import DbConnection


class Sale(DbConnection):
 
   
    def addSale(self, product_id, quantity, total_price): 
        self.requester = 1       
        command = """INSERT INTO sales (attendant_id, product_id,
        quantity, total_price) VALUES ( %s, %s, %s, %s) """
        self.cursor.execute(
            command, 
            (self.requester, product_id, quantity, total_price)                         
        )          
        return {
            "product_id": product_id,            
            "quantity": quantity,
            "total_price": total_price
            } 

    def getAllRecords(self):
        command = """SELECT sale_id, sales.product_id, product_name, unit_price, sales.quantity, 
                        total_price,attendant_id, created_at FROM products JOIN sales ON 
                        (products.product_id=sales.product_id)"""                          
        self.cursor.execute(command)
        return self.cursor.fetchall()  

    def getRecordById(self, sale_id):
        command = """SELECT sale_id, sales.product_id, product_name, unit_price, sales.quantity, 
                        total_price,attendant_id, created_at FROM products JOIN sales ON 
                        (products.product_id=sales.product_id) WHERE sale_id = %s"""                                                           
        self.cursor.execute(command, [sale_id])
        return self.cursor.fetchone()      
        
    def updateProductQuantity(self, product_id, new_quantity):   
        command = """UPDATE products SET quantity = %s WHERE product_id = %s """    
        self.cursor.execute(command, (new_quantity, product_id))
        

         