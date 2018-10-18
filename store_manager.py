inventory = [] #list of all added products + details 

class Product_Operation:

    def admin_create_product(self, name, unit_of_measure, unit_price 
                            ,initial_quantity, minimum_quantity):

        """This method will add a dictionary of the  product details 
        to the inventory list after checking that this product is not 
        already in the inventory list.
        """
        product_duplicate = False #set variable that will be toggled incase a duplicate is found
        if len(inventory) > 0:              
            for product in inventory:                
                if product["product_name"] == name:
                    product_duplicate = True   

        if product_duplicate:                    
            self.response = "Product already exists!"
            return False   
        else:  
            inventory.append({"product_id":len(inventory)+1
                        ,"product_name":name
                        ,"unit_of_measure":unit_of_measure
                        ,"unit_price":unit_price
                        ,"quantity":initial_quantity
                        ,"minumum_quantity":minimum_quantity
                        })      
            self.response = "Product added to inventory successfully!"
            return True                   
        
    def get_product_by_id(self,product_id):
        """method to get back dictionary of product details from inventory
        list when the user supplies the product id.
        """
        for product in inventory:
            if product["product_id"] == product_id:
                return product    
                
      

# if __name__ == '__main__':     


    
    
