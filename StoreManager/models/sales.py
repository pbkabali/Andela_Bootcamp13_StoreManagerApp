from datetime import datetime

# """dictionary of sales records from all attendants"""
sales_records = {"records":[],"total_sales":0} 


class Sale:
    
    def __init__(self, product_name, quantity, unit_price, requester):
        self.sale_id = len(sales_records["records"])+1
        self.product_name = product_name        
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = quantity*unit_price
        self.requester = requester
        self.created_at = datetime.now()
        self.record_details ={
            "sale_id":self.sale_id
            ,"product_name":self.product_name
            ,"quantity":self.quantity
            ,"unit_price":self.unit_price
            ,"total_price":self.total_price
            ,"requester":self.requester
            ,"created_at": self.created_at
        }

    
        
        
        