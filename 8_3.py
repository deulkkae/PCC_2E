'''
def get_formatted_name(first_name, middle_name, last_name):
    """읽기 쉬운 전체 이름을 반환합니다"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)
'''
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    """읽기 쉬운 전체 이름을 반환합니다"""

    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hooker', 'lee')
print(musician)
'''
'''
def build_person(first_name, last_name, age=None):
    """사람에 관한 정보 딕셔너리를 반환합니다"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
'''
'''
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환한다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 이건 무한 루프다
while True: 
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name =='q':
        break
    l_name = input("Last name: ")
    if f_name =='q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
'''
'''
# 연습문제 8-6
def city_country(city, country):
    """도시와 국가 이름을 받는 함수"""
    full_name = f"{city}, {country}"
    return full_name.title()

name = city_country('seoul', 'south korea')
print(name)
name = city_country('jeju', 'south korea')
print(name)
name = city_country('pyeongyang', 'north korea')
print(name)
'''
# 연습문제 8-7
def make_album(name, title, number=None):
    full_name = {'singer': name, 'song': title }
    if number: 
        full_name['number'] = number
    return full_name

while True:
    print("\nPlease tell me any singer and song")
    print("(enter 'q' at any time to quit)")
    name = input("Singer: ")
    if name == 'q':
        break
    title = input("Song: ")
    if title == 'q':
        break
    number = input("Number: ")
    if title == 'q':
        break

    name = make_album(name, title, number)
    print(name)
