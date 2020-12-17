'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

'''
for alien in aliens[:5]:
    print(alien)

print(f"total number of aliens: {len(aliens)}")
'''
'''
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
'''
'''
pizza = {
    'crust' : 'thick',
    'toppings': ['mushrooms', 'extra chees'],
}
# 주문 요약입니다.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")
'''
'''
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is: ")
    else:
        print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages: 
        print(f"\t{language.title()}")
'''
'''
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")
'''
# 연습문제
'''
users = {
    '윤나리': {
    'first_name': '나리',
    'last_name': '윤',
    'age': 32,
    'city': 'Seoul'
    },
    '안다빈': {
    'first_name': '다빈',
    'last_name': '안',
    'age': 32,
    'city': 'Seoul'
    },
    '윤다정': {
    'first_name': '다정',
    'last_name': '윤',
    'age': 35,
    'city': 'Seoul'
    }
}
people = ['윤나리', '안다빈', '윤다정']

for user, user_info in users.items():
    print(f"{user}")
    print(f"{user_info['age']}")
    print(f"{user_info['city']}\n")
'''
'''
nari = {'first_name': '나리', 'last_name': '윤', 'age': 32, 'city': 'Seoul'}
dave = {'first_name': '다빈', 'last_name': '안', 'age': 32, 'city': 'Seoul'}
dajung = {'first_name': '다정', 'last_name': '윤', 'age': 35, 'city': 'Seoul'}

users = [nari, dave, dajung]

for user in users:
    print(user)
'''
'''
dog_1 = {'name': '복순이', 'owner': '복희'}
dog_2 = {'name': '방울이', 'owner': '나리'}

pets = [dog_1, dog_2]

for dog in pets:
    print(dog)
'''
'''
favorite_places = {
    '윤나리': {
        'place_1': '서울',
        'place_2': '대전',
        'place_3': '대구',
        },
    '안다빈': {
        'place_1': '울산',
        'place_2': '광주',
        'place_3': '제주',
        },
    '윤다정': {
        'place_1': '평양',
        'place_2': '제주',
        'place_3': '부산',
        }
}

for name, place_info in favorite_places.items():
    print(f"{name}'s the first loving place is {place_info['place_1']}.")


favorite_number = {
    '다빈' : '1, 7, 4',
    '나리' : '3, 5, 9',
    '다정' : '7, 8',
    '병산' : '2, 11',
    '해북' : '11, 3'
}

for person, favorite in favorite_number.items():
    print(f"{person}'s favorite_numbers are {favorite}")
'''

cities = {
    '서울':{
        'country' : '대한민국',
        'population' : '1000만',
        'fact': '좋음',
    },
    '대전':{
        'country' : '대한민국',
        'population' : '100만',
        'fact': '나쁨',
    },
    '부산':{
        'country' : '대한민국',
        'population' : '80만',
        'fact': '별로',
    }
}

for city, city_info in cities.items():
    print(f"{city}:")
    print(f"\tcountry: {city_info['country']}")
    print(f"\tpopulation: {city_info['population']}")
    print(f"\tcountry: {city_info['country']}")
