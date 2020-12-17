'''
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for k, v in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

'''
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())
'''
'''
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
'''
'''
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())
'''

# 연습문제
'''
cities = {
    '나일': '이집트',
    '한강': '대한민국',
    '센강': '파리',
    '템스강': '런던',
    '메콩': '비엔티엔'
}
for key, value in cities.items():
    print(key)

for key, value in cities.items():
    print(value)

for key, value in cities.items():
    print(f"{key}은 {value}의 강이다.")
'''


people = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
already_voted = {
    'aaa': 'python',
    'fff': 'java',
    'zzz': 'python',
    'ccc': 'c',
    'xxx': 'ruby'
}

for man in people:
    if man in already_voted.keys():
        print(f"{man.title()}, you already voted!")
    else:
        print(f"{man.title()}, you should vote today.")