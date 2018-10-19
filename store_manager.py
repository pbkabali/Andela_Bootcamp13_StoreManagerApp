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
# """dictionary of sales records from all attendants"""
sales_records = {"total_sales":0, "total_products_sold":0} 

# """dictionary to hold cart temporarily"""

shopping_cart = {"total_price":0, "total_items_in_cart":0}

initial_shopping_cart = {"total_price":0, "total_items_in_cart":0}


class Product_Operation:

    def __init__(self, requester):              
        self.requester = requester      
        
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
            id_in_cart = len(shopping_cart)-1 # subtract the two addional rows of 
                                                        #total items and total price         
            shopping_cart[str(id_in_cart)] = {
                "product_name":inventory[product_id]["product_name"]
                ,"quantity_ordered":quantity
                ,"price": quantity*inventory[product_id]["unit_price"]
            }           
            shopping_cart["total_price"] += quantity*inventory[product_id]["unit_price"]
            shopping_cart["total_items_in_cart"] += quantity         

            inventory[product_id]["quantity"] -= quantity

            self.response = "Product added to cart successfully!"

    def create_sales_record(self):  
        global shopping_cart      
        shopping_cart["created-by"] = self.requester
        shopping_cart["created_at"] = datetime.now()            
        sales_records[str(len(sales_records)-1)] = shopping_cart            
        sales_records["total_sales"] += shopping_cart["total_price"]
        sales_records["total_products_sold"] += shopping_cart["total_items_in_cart"]
        shopping_cart = initial_shopping_cart
        self.response = "Sales Record Created Successfully"

    def  get_record_by_id(self, sale_id):
        """method to get back dictionary of specific sale details from sales_record
        dictionary when the user supplies the sale id.
        """
        return sales_records[sale_id]          
      

# if __name__ == '__main__':     


    
    
