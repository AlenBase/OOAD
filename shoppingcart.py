
class LogicError:
    pass

class ShoppingCart:
    
    def __init__(self) -> None:
        self.__head = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,anun):
        self.__name = anun
        
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self,qanak):
        self.__quantity = qanak
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value == '' or value <= 0:
            raise LogicError('Not valid operation')
        self.__price = value
    
    def add_product(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.__head.append((name,quantity,price))
        
    def remove_product(self,name):
        for item in self.__head:
            if item[0] == name:
                self.__head.remove(item)
                break
    
    
    def calculate_total(self):
        if not self.__head:
            print('Your basket is empty.')
            return
        total_price = sum(item[2] for item in self.__head)
        print(f'Total price: {total_price}')
                
            
    
    def view_products(self):
        if not self.__head:
            print('Your basket is empty.')
        else:
            for item in self.__head:
                print(f'Name: {item[0]}, Quantity: {item[1]}, Price: {item[2]}')





obj = ShoppingCart()
obj.add_product('Xndzor',3,100)
obj.add_product('Tandz',4,200)
obj.view_products()
obj.remove_product('Xndzor')
obj.view_products()



