'''
class Dog: # 클래스를 정의, 클래스 이름의 첫 글자는 대문자로 쓴다
    """개를 모델화하는 시도"""

    #클래스에 속한 함수를 메서드라고 한다
    def __init__(self, name, age): # __init__() 메서드는 개별 개의 인스턴스를 만들고 name과 age 속성의 값을 설정한다
        """name과 age 속성 초기화"""
        self.name = name # 인스턴스에서 접근할 수 있는 변수를 속성이라고 부른다
        self.age = age

    def sit(self):
        """명령에 따라 앉는 개"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """명령에 따라 구르는 개"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit() # sit() 메서드 호출!
my_dog.roll_over() # roll_over() 메서드 호출!

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit() # sit() 메서드 호출!
your_dog.roll_over() # roll_over() 메서드 호출!
'''

'''
# 연습문제 9-1
class Restaurant: 
    """레스토랑의 이름과 종류를 모델화"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant1 = Restaurant('우래옥', '냉면집')
restaurant2 = Restaurant('사이공레시피', '베트남음식점')
restaurant3 = Restaurant('교촌치킨', '치킨집')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.open_restaurant()
'''

# 연습문제 9-2
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

user1 = User('Deulkkae', 'Soondubu', 33, 'online')
user1.describe_user()
user1.greet_user()