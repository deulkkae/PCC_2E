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


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(f"\n{my_used_car.get_descriptive_name()}")

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.inccrememt_odometer(-50)
my_used_car.read_odometer()
'''

'''
# 연습문제 9-4
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

restaurant1 = Restaurant('우래옥', '냉면집')
restaurant1.read_served_times()
restaurant1.set_served_times(5)
restaurant1.read_served_times()
restaurant1.increment_served_times(10)
restaurant1.read_served_times()
'''

# 연습문제 9-5
class User:
    """사용자 이름과 프로필 정보를 모델화"""

    def __init__(self, first_name, last_name, age, status):
        """사용자 속성 초기화"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.login_attempts = 0

    def describe_user(self):
        """유저 정보 출력"""
        print(f"{self.first_name} {self.last_name} is {self.age} years old and now {self.status}.")

    def greet_user(self):
        """유저에게 인사말 출력"""
        print(f"Hi, {self.first_name} {self.last_name}, good to see you!")

    def increment_login_attempts(self):
        """로그인 시도 1회 추가"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """로그인 시도 초기화"""
        self.login_attempts = 0

user1 = User('Deulkkae', 'Soondubu', 33, 'online')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)