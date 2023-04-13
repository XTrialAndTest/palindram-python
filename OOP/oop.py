class OOP:
    def __init__(self,name:str,quantity:int,price:float):
        assert quantity>0, "quantity must be positive number"
        assert price>0, "price must be positive number"
        self.__name = name
        self.quantity = quantity
        self.price = price
        @property()
        def name(self):
            return self.__name


class InventoryManagment(OOP):
    def __init__(self,name:str,quantity:int,price:float):
        super().__init__(name,quantity,price)
    def add_item(self):
        pass
    def remove_item(self):
        pass
    def update_item(self):
        pass 
    def display_item(self):
        pass


item=InventoryManagment('john',6,150.65)
item.add_item()
item.name='mwangi'
print(item.name)