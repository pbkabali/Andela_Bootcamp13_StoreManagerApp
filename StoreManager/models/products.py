# """#dictionary of all added products + details"""
inventory = [] 

class Product:
    
    def __init__(
        self, category, name, unit_of_measure
        ,unit_price, quantity, minimum_quantity
    ):              
        self.product_id = len(inventory)+1
        self.category = category
        self.name = name
        self.unit_of_measure = unit_of_measure
        self.unit_price = unit_price
        self.quantity_to_add = quantity
        self.minimum_quantity = minimum_quantity
        self.product_details = {
            "product_id": self.product_id
            ,"category" : self.category
            ,"name":self.name
            ,"unit_of_measure":self.unit_of_measure
            ,"unit_price":self.unit_price
            ,"quantity":self.quantity_to_add
            ,"minumum_quantity":self.minimum_quantity
        }   
        
        
        

      