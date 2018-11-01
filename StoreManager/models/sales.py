
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

    def getAllRecords(self):
        command = """SELECT * FROM sales JOIN products ON product_id = products.id """                          
        self.cursor.execute(command)
        return self.cursor.fetchall()  

    def getRecordById(self, sale_id):
        command = """SELECT * FROM sales s JOIN products p ON s.product_id = p.id WHERE s.id = %s"""                                
        self.cursor.execute(command, [sale_id])
        return self.cursor.fetchone()      
        
    def updateProductQuantity(self, product_id, new_quantity):   
        command = """UPDATE products SET quantity = %s WHERE id = %s """    
        self.cursor.execute(command, (product_id, new_quantity))
        

         