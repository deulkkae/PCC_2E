from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_telsa = ElectricCar('telsa', 'roadster', 2019)
print(my_telsa.get_descriptive_name())
