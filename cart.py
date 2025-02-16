class Cart:
    def __init__(self):
        self.items = []
        self.total_amount = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            print(f'Added to cart: {amount} of {device}')

    def remove_device(self, device, amount):
        for index, (item_device, quantity) in enumerate(self.items):
            if item_device == device:
                if amount >= quantity:
                    self.items.pop(index)
                else:
                    self.items[index] = (item_device, quantity - amount)
                return

        print(f"{device.name} is not in the cart.")  # Runs if device was not found

    def calculate_total(self):
        self.total_amount = sum([item[1] for item in self.items])

    def checkout(self):
        if not self.items:
            print('There are no items in cart')
            return

        for device, quantity in self.items:
            if not device.is_available(quantity):
                print(f'Not enough stock for {device.name}')

        for device, quantity in self.items:
            device.reduce_stock(quantity)

        for device, quantity in self.items:
            print(f'''Receipt{quantity} x {device.name} - ${device.price} each
        f"Total Amount: ${self.calculate_total()}''')

