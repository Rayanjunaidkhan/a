class product:
    def __init__(self,produt_name,product_price):
        self.product_price = product_price
        self.product_name = produt_name

    def display_info(self):
        print(f"Name: {self.product_name}, price: {self.product_price}")

class electronic(product):
    def __init__(self, produt_name, product_price,warranty_period):
        super().__init__(produt_name, product_price)
        self.warrenty_period = warranty_period

    def display_warranty(self):
        print(f"warranty period is {self.warrenty_period} years")

    def display_info(self):
        print(f"Name: {self.product_name}, price: {self.product_price}, warrenty is {self.warrenty_period} years")

class clothing(product):
    def __init__(self, produt_name, product_price,size):
        super().__init__(produt_name, product_price)
        self.size = size

    def display_size(self):
        print(f"product size is {self.size}")
    
    def display_info(self):
        print(f"Name: {self.product_name}, price: {self.product_price}, size is {self.size}")
    
    
instance1 = electronic("laptop",1000,2)
instance2 = clothing("T-shirt",20,"M")

instance1.display_info()   
instance1.display_warranty()
instance2.display_info()
instance2.display_size()
        