from car import ElectricCar

my_telsa = ElectricCar('telsa', 'model s', 2019)

print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()