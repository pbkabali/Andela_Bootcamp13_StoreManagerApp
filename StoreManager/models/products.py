# """#dictionary of all added products + details"""
inventory = {} 

class Product:
    
    def __init__(
        self, name, unit_of_measure, unit_price 
                            ,quantity, minimum_quantity
    ):              
        self.product_id = len(inventory)+1
        self.name = name
        self.unit_of_measure = unit_of_measure
        self.unit_price = unit_price
        self.quantity_to_add = quantity
        self.minimum_quantity = minimum_quantity     
        
    def create_product(self):
        """This method will add a dictionary of the  product details 
        to the inventory  after checking that this product is not 
        already in the inventory list.
        """
        product_duplicate = False #set variable that will be toggled incase a duplicate is found
        if len(inventory) > 0:              
            for product in inventory:                
                if inventory[product]["product_name"] == self.name:
                    product_duplicate = True   

        if product_duplicate:                    
            return False
             
        else:  
            inventory[self.product_id] = {
                        "product_name":self.name
                        ,"unit_of_measure":self.unit_of_measure
                        ,"unit_price":self.unit_price
                        ,"quantity":self.quantity_to_add
                        ,"minumum_quantity":self.minimum_quantity
                        }                  
            return True                   