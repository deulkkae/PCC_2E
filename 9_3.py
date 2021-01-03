'''
class Car:
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """알아보기 쉬운 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """주행거리를 주어진 값으로 바꿈"""
        """주행거리를 더 작은 값으로 바꾸려고 하면 거부"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("Yon can't roll back an odometer!")

    def inccrememt_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘린다"""
        if miles < 0:
            print("Yon can't roll back an odometer!")
        else:
            self.odometer_reading += miles

class Battery:
    """전기 자동차의 배터리를 모델화하려는 단순한 시도"""

    def __init__(self, battery_size=75):
        """배터리 속성 초기화"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """배터리 크기를 설명하는 문장 출력"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """배터리가 제공하는 주행 가능 거리를 출력한다"""

        if self.battery_size == 75:
            range = 250
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """전기 자동차에만 해당하는 특징을 나타낸다"""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화하고
        전기자동차에만 해당하는 속성을 초기화한다
        """
        super().__init__(make, model, year) # super()는 부모 클래스를 호출하는 함수
        self.battery = Battery()

    def fill_gas_tank(self): # Car 클래스에 이 메서드가 있다고 가정하고 여기서 오버라이드
        """전기 자동차에는 연료 탱크가 없습니다."""
        print("This car doesn't need a gas tank!")

my_telsa = ElectricCar('telsa', 'model s', 2019)
print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
'''

# 연습문제 9-6
'''
class Restaurant: 
    """레스토랑의 이름과 종류를 모델화"""

    def __init__(self, restaurant_name, cuisine_type):
        """레스토랑의 이름과 종류 속성 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """레스토랑의 종류 출력"""
        print(f"{self.restaurant_name} is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """레스토랑이 열었는지 확인"""
        print(f"{self.restaurant_name} is now open.")
    
    def read_served_times(self):
        """서빙한 횟수 출력"""
        print(f"{self.number_served} times served.")

    def set_served_times(self, times):
        """서빙한 횟수 변경"""
        self.number_served = times
    
    def increment_served_times(self, aday):
        self.number_served += aday

class IceCreamStand(Restaurant):
    """레스토랑 클래스를 상속하는 아이스크림 클래스"""

    def __init__(self, restaurant_name, cuisine_type):
        """부모 클래스의 속성을 초기화"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'basic'
    
    def get_flavors(self, ordered_flavor):
        self.flavors = ordered_flavor
    
    def descrive_flavors(self):
        print(f"You ordered {self.flavors} icecream.")

my_icecream = IceCreamStand('베스킨라빈스', '아이스크림 가게')
my_icecream.get_flavors('choco')
my_icecream.descrive_flavors()
'''

# 연습문제 9-7/8
'''
class User:
    """사용자 이름과 프로필 정보를 모델화"""

    def __init__(self, first_name, last_name, age, status):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and now {self.status}.")

    def greet_user(self):
        print(f"Hi, {self.first_name} {self.last_name}, good to see you!")

class Privileges:

    def __init__(self, privilege='add post, delete post, ban user'):
        """권한의 속성 초기화"""
        self.privilege = privilege
    
    def show_privileges(self):
        print(f"This user can {self.privilege}")


class Admin(User):
    """User 클래스를 상속하는 Admin 클래스"""

    def __init__(self, first_name, last_name, age, status):
        """부모 클래스의 속성을 초기화"""
        super().__init__(first_name, last_name, age, status)
        self.privileges = Privileges()


user1 = User('Deulkkae', 'Soondubu', 33, 'online')
user1.describe_user()
user1.greet_user()
user2 = Admin('Matt', 'Damon', 36, 'online')
user2.privileges.show_privileges()
'''

# 연습문제 9-9
'''
class Car:
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """알아보기 쉬운 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """주행거리를 주어진 값으로 바꿈"""
        """주행거리를 더 작은 값으로 바꾸려고 하면 거부"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("Yon can't roll back an odometer!")

    def inccrememt_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘린다"""
        if miles < 0:
            print("Yon can't roll back an odometer!")
        else:
            self.odometer_reading += miles

class Battery:
    """전기 자동차의 배터리를 모델화하려는 단순한 시도"""

    def __init__(self, battery_size=75):
        """배터리 속성 초기화"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """배터리 크기를 설명하는 문장 출력"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """배터리가 제공하는 주행 가능 거리를 출력한다"""

        if self.battery_size == 75:
            range = 250
        elif self.battery_size == 85:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """베터리 크기 확인하고 용량 바꾸기"""
        
        if self.battery_size != 85:
           self.battery_size = 85

class ElectricCar(Car):
    """전기 자동차에만 해당하는 특징을 나타낸다"""

    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화하고
        전기자동차에만 해당하는 속성을 초기화한다
        """
        super().__init__(make, model, year) # super()는 부모 클래스를 호출하는 함수
        self.battery = Battery()

    def fill_gas_tank(self): # Car 클래스에 이 메서드가 있다고 가정하고 여기서 오버라이드
        """전기 자동차에는 연료 탱크가 없습니다."""
        print("This car doesn't need a gas tank!")

my_telsa = ElectricCar('telsa', 'model s', 2019)
print(my_telsa.get_descriptive_name())
my_telsa.battery.describe_battery()
my_telsa.battery.get_range()
my_telsa.battery.upgrade_battery()
my_telsa.battery.get_range()
'''

# 연습문제 9-14
from random import randint
x = randint(1, 6)

class Die:
    """주사위 클래스"""

    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        print(x)

dice1 = Die(10)
dice1.roll_die()