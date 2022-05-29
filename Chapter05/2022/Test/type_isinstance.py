from typing import List


class Computer:
    def __init__(self, name: str, cpu_name: str, gpu_name: str):
        self.name = name
        self.cpu_name = cpu_name
        self.gpu_name = gpu_name

    def get_info(self):
        print(f"name    : {self.name}")
        print(f"cpu name: {self.cpu_name}")
        print(f"gpu name: {self.gpu_name}")


class Desktop(Computer):
    def __init__(self, name: str, cpu_name: str, gpu_name: str, power_name: str):
        super().__init__(name, cpu_name, gpu_name)
        self.power_name = power_name

    def get_power_info(self):
        super().get_info()
        print(f"power info: {self.power_name}")


class Laptop(Computer):
    def __init__(self, name: str, cpu_name: str, gpu_name: str, battery_name: str):
        super().__init__(name, cpu_name, gpu_name)
        self.cpu_name = cpu_name
        self.gpu_name = gpu_name
        self.battery_name = battery_name

    def get_battery_info(self):
        super().get_info()
        print(f"battery info: {self.battery_name}")


if __name__ == "__main__":
    my_computer: Laptop = Laptop('AMD Laptop','AMD Rygen 5', 'Radeon', 'ABC Battery')
    your_computer: Laptop = Laptop('Intel Laptop','Intel i5', 'RTX 3060', 'DEF Battery')

    print(f"type(my_computer)  : {type(my_computer)}")
    print(f"type(your_computer): {type(your_computer)}")
    print()

    print(f"type(my_computer) == Computer: {type(my_computer) == Computer}")
    print(f"type(my_computer) == Desktop : {type(my_computer) == Desktop}")
    print(f"type(my_computer) == Laptop  : {type(my_computer) == Laptop}")
    print()

    print(f"isinstance(my_computer, Computer): {isinstance(my_computer, Computer)}")
    print(f"isinstance(my_computer, Desktop) : {isinstance(my_computer, Desktop)}")
    print(f"isinstance(my_computer, Laptop)  : {isinstance(my_computer, Laptop)}")
    print()

    print(f"type(my_computer).get_battery_info: {type(my_computer).get_battery_info}")
    print(f"my_computer.get_battery_info      : {my_computer.get_battery_info}")
    print()

    print("type(my_computer).get_battery_info(my_computer):")
    type(my_computer).get_battery_info(my_computer)
    print()
    print("my_computer.get_battery_info():")
    my_computer.get_battery_info()
    print()

    print("type(my_computer).get_battery_info(your_computer):")
    type(my_computer).get_battery_info(your_computer)
    print()
    # error
    print("my_computer.get_battery_info(your_computer): error")
    # my_computer.get_battery_info(your_computer)
    print()
