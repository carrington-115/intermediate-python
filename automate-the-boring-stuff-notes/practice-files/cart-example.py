# cart example with the OOP paradigm
cart_items = []

class Cart_product:
    def __init__(self, product_name, price, buyer_name, seller_name, delivery_location, delivery_date):
        self.product_name = product_name
        self.price = price
        self.buyer_name = buyer_name
        self.seller_name = seller_name
        self.delivery_location = delivery_location
        self.delivery_date = delivery_date

    def product_details(self):
        return {
            "Product name": self.product_name,
            "Price": self.price,
            "Buyer": self.buyer_name,
            "Seller": self.seller_name,
            "Delivery location": self.delivery_location,
            "Delivery date": self.delivery_date
        }
    
    @property
    def product_name(self):
        return self._product_name
    
    @product_name.setter
    def name(self, product_name):
        if not product_name:
            raise ValueError('Invalid name')
        self.product_name = product_name
    
class Cart:
    def __init__(self, cart_data):
        self.cart_data = cart_data

    def __str__(self):
        print('This is the cart')


def new_item():
    product_name = input('Name: ')
    price = input('Price: ')
    buyer_name = input('Buyer name: ')
    seller_name = input('Seller name: ')
    delivery_location = input('Location: ')
    delivery_date = input('Delivery date: ')
    product = Cart_product(product_name, price, buyer_name, seller_name, delivery_location, delivery_date)
    return product.product_details()

def main():
    item = new_item()
    print(item)

if __name__ == "__main__":
    main()