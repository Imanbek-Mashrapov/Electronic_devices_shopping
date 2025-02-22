from device_subclasses.smartphone import Smartphone
from device_subclasses.laptop import Laptop
from device_subclasses.tablet import Tablet
from device import Device
from cart import Cart


if __name__ == '__main__':
    devices = [
        Smartphone("iPhone 15", 1299, 10, 6.1, 20),
        Smartphone("Samsung Galaxy S23", 1199, 15, 6.5, 25),
        Smartphone("Google Pixel 8", 999, 12, 6.3, 24),
        Smartphone("OnePlus 11", 899, 8, 6.7, 22),
        Smartphone("Xiaomi 13 Pro", 799, 20, 6.8, 30),

        Laptop("MacBook Pro 16", 2499, 5, "3456x2234", 2000),
        Laptop("Dell XPS 15", 1899, 7, "3840x2400", 1800),
        Laptop("HP Spectre x360", 1599, 6, "1920x1080", 1400),
        Laptop("Lenovo ThinkPad X1", 1799, 10, "2560x1600", 1200),
        Laptop("ASUS ROG Zephyrus", 2199, 4, "2560x1440", 2500),

        Tablet("iPad Pro 12.9", 1299, 15, "2048x2732", 682),
        Tablet("Samsung Galaxy Tab S9", 1099, 8, "2560x1600", 567),
        Tablet("Microsoft Surface Pro 9", 999, 9, "2880x1920", 879),
        Tablet("Lenovo Tab P12", 749, 12, "2000x1200", 600),
        Tablet("Huawei MatePad Pro", 899, 11, "2800x1752", 620),

        Smartphone("Sony Xperia 5 IV", 999, 7, 6.1, 21),
        Laptop("Acer Swift X", 1299, 9, "1920x1080", 1500),
        Tablet("Amazon Fire HD 10", 149, 25, "1920x1200", 465),
        Smartphone("Nothing Phone 2", 599, 10, 6.55, 18),
        Laptop("Razer Blade 14", 2399, 3, "2560x1440", 2100)
    ]

    for device in devices:
        if isinstance(device, Smartphone):
            device_type = "Smartphone"
        elif isinstance(device, Laptop):
            device_type = "Laptop"
        elif isinstance(device, Tablet):
            device_type = "Tablet"
        else:
            device_type = "Unknown Device"

        print(f"#{devices.index(device) + 1} Type: {device_type}: {device.display_info()}")

    my_cart = Cart()
    print()
    print(f"Your cart: {my_cart.items}")
    print()

    while True:
        try:
            choice = int(input('Enter the option number #: '))
            device_num = int(input('Enter the amount of devices: '))

            if choice < 1 or choice > len(devices):
                print("Error: Invalid option number. Please try again.")
                continue

            if device_num <= 0:
                print("Error: Amount must be a positive number.")
                continue

            my_cart.add_device(devices[choice - 1], device_num)
            print("\nCurrent Cart:")
            my_cart.print_items()
            stop = input("Do you want to exit? (1 = Yes, 0 = No): ").strip()
            if stop == "1":
                print('Thanks for your purchases')
                break

        except ValueError:
            print('Error: Amount and option number must be numeric.')





