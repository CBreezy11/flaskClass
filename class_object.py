class Store():
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        return self.items.append({"name": name, "price": price})
    
    def stock_price(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")    
        
    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))


my_store = Store('brandon')
my_store.add_item('oats', 5)
my_store.add_item('eggs', 3)
print(my_store.stock_price())
Store.franchise(my_store)
print(Store.store_details(Store.franchise(my_store)))