from device import Device
from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet


if __name__ == '__main__':
    phone1 = Smartphone('Samsung', 500, 10, '10*10', 3000, warranty_period=6)
    print(phone1.display_info())
    print()
    laptop1 = Laptop("MacBook Pro", 1999, 15, 16, 3.2)
    print(laptop1.display_info())
    print()
    tablet1 = Tablet("iPad Pro", 1099, 25, "2048x1536", 468)
    print(tablet1.display_info())
