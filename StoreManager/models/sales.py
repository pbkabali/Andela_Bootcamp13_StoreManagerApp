# """dictionary of sales records from all attendants"""
sales_records = {"total_sales":0, "total_products_sold":0} 


class Sale:
    
    def __init__(self, requester, cart_details, created_at, total_items, total_sales):
        self.sale_id = str(len(sales_records)-1)
        self.requester = requester
        self.cart_details = cart_details
        self.created_at = created_at
        self.total_items = total_items
        self.total_sales = total_sales

    def create_record(self):     
        sales_records[self.sale_id] = self.cart_details          
        sales_records[self.sale_id]["created_by"] = self.requester
        sales_records[self.sale_id]["created_at"] = self.created_at
        sales_records["total_sales"] += self.total_sales
        sales_records["total_products_sold"] += self.total_items
        