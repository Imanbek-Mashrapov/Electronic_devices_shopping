from device import Device
from smartphone import Smartphone


if __name__ == '__main__':
    phone1 = Smartphone('Samsung', 500, 10, '10*10', 3000, warranty_period=6)
    print(phone1.display_info())