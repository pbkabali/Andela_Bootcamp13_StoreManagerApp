from datetime import datetime

inventory = {   #dictionary of all added products + details 
    1: {
        "product_name": "baseball_hats"
        ,"unit_of_measure": "pcs"
        ,"unit_price": 10
        ,"quantity": 35
        ,"minumum_quantity":2
    } 
    
    ,2: {
        "product_name": "blue_jeans"
        ,"unit_of_measure": "pairs"
        ,"unit_price": 25
        ,"quantity": 80
        ,"minumum_quantity":5
    } 
    ,3: {
        "product_name": "mens_vests"
        ,"unit_of_measure": "pcs"
        ,"unit_price": 8
        ,"quantity": 54
        ,"minumum_quantity":10
    } 
}  
"""dictionary of sales records from all attendants"""
sales_records = {} 

class Product_Operation:

    def __init__(self, requester):              
        self.requester = requester
        self.shopping_cart = {}
        self.total_price_in_cart = 0
        self.total_items_in_cart = 0

    def admin_create_product(self, name, unit_of_measure, unit_price 
                            ,initial_quantity, minimum_quantity):

        """This method will add a dictionary of the  product details 
        to the inventory  after checking that this product is not 
        already in the inventory list.
        """
        product_duplicate = False #set variable that will be toggled incase a duplicate is found
        if len(inventory) > 0:              
            for product in inventory:                
                if inventory[product]["product_name"] == name:
                    product_duplicate = True   

        if product_duplicate:                    
            self.response = "Product already exists! Choose edit instead"
            return False   
        else:  
            inventory[len(inventory)+1] = {
                        "product_name":name
                        ,"unit_of_measure":unit_of_measure
                        ,"unit_price":unit_price
                        ,"quantity":initial_quantity
                        ,"minumum_quantity":minimum_quantity
                        }      
            self.response = "Product added to inventory successfully!"
            return True                   
        
    def get_product_by_id(self,product_id):
        """method to get back dictionary of product details from inventory
        dictionary when the user supplies the product id.
        """
        return inventory[product_id]  


    def add_to_cart_by_id(self, product_id, quantity):

        if product_id > len(inventory):
            self.response = "Product not found!"

        elif inventory[product_id]["quantity"] < quantity:
            self.response = "Not enough quantity in inventory!"

        else: 
            if len(self.shopping_cart) == 0:
                id_in_cart = 1
            else:    
                id_in_cart = len(self.shopping_cart)-1 # subtract the two addional rows of 
                                                        #total items and total price         
            self.shopping_cart[str(id_in_cart)] = {
                "product_name":inventory[product_id]["product_name"]
                ,"quantity_ordered":quantity
                ,"price": quantity*inventory[product_id]["unit_price"]
            }
            self.total_price_in_cart += quantity*inventory[product_id]["unit_price"]
            self.total_items_in_cart += quantity
            self.shopping_cart["total_price"] = self.total_price_in_cart
            self.shopping_cart["total_items_in_cart"] = self.total_items_in_cart

            inventory[product_id]["quantity"] -= quantity

            self.response = "Product added to cart successfully!"

    def create_sales_record(self):
            self.shopping_cart["created-by:"] = self.requester
            self.shopping_cart["created_at:"] = datetime.now()            
            sales_records[len(sales_records)+1] = self.shopping_cart
            # self.shopping_cart.clear() - check ehy this clears all sales records
            self.response = "Sales Record Created Successfully"

            






                
      

# if __name__ == '__main__':     


    
    
