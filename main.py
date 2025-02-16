from device import Device
from smartphone import Smartphone
from laptop import Laptop


if __name__ == '__main__':
    phone1 = Smartphone('Samsung', 500, 10, '10*10', 3000, warranty_period=6)
    print(phone1.display_info())

    laptop1 = Laptop("MacBook Pro", 1999, 15, 16, 3.2)
    print(laptop1.display_info())