'''
def greet_user(username):
    """간단한 환영 인사를 표시한다"""
    print(f"hello, {username.title()}!")

greet_user('jesse')

def display_message():
    """간단한 메시지를 출력한다"""
    print(f"파이썬 열공 중!")

display_message()

def favorite_book(name, title):
    """좋아하는 책을 출력해보자"""
    print(f"{name}가 좋아하는 책은 {title}이다.")

favorite_book('나리', '김치도감')
'''
'''
def describe_pet(animal_type, pet_name):
    """반려동물에 관한 정보를 출력한다."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(animal_type='hamster', pet_name= 'harry')
describe_pet(animal_type='dog', pet_name= 'whillie')
'''
'''
def describe_pet(pet_name, animal_type='dog'):
    """반려동물에 관한 정보를 출력한다."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('whillie')
describe_pet(animal_type='hamster', pet_name= 'harry')
describe_pet()
'''

# 연습문제
def make_shirt(message, size='L' ):
    """티셔츠 사이즈와 티셔츠에 인쇄할 메시지를 요약해 출력한다"""
    print(f"이 {size}의 티셔츠에는 '{message}'를 인쇄한다")

make_shirt('L 사이즈 입니다.')
make_shirt('S 사이즈 입니다.', 'S')

def describe_city(city, country='대한민국'):
    """도시 이름과 나라 이름을 출력한다"""
    print(f"{city}는 {country}에 있다.")

describe_city('서울')
describe_city('도쿄', '일본')
describe_city('대구')

