from device import Device


class Laptop(Device):
    def __init__(self, name, price, stock, ram_size, processor_speed, warranty_period=12):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def run_program(self, program_name):
        print(f'{self.name} is running {program_name}...')

    def use_keyboard(self, typing_word='qwerty'):
        print(f"Typing '{typing_word}' on {self.name} keyboard...")

    def display_info(self):
        return f'''Name: {self.name}, 
Price: {self.price}$, 
Stock: {self.stock}, 
Warranty period: {self.warranty_period} months,
RAM size: {self.ram_size} GB,
Processor size: {self.processor_speed} GHz'''
