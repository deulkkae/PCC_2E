"""
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registed to vote yet?")
else: 
    print("Sorry, you are too young yo vote.")
    print("Please register to vote as soon as you turn 18!")

age = 62
if age <4:
    price = 0
    print("free")
elif age<18:
    price = 25
elif age<65:
    price = 40
elif age>65:
    price = 10

print(f"당신의 입장료는 ${price}입니다.")


alien_color = 'yellow'
if alien_color == 'green':
    print("You got s5 points!")
else:
    print("You fool!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You got s5 points!")
if alien_color != 'green':
    print("You fool!")


age = 67
if age <2:
    print("baby")
elif age <4:
    print("toddler")
elif age <13:
    print("kid")
elif age <20:
    print("teenager")
elif age < 65:
    print("adult")
else: 
    print("elder")
"""
"""
favorite_fruits = ['사과', '배', '복숭아', '수박', '체리']
fruit = ['사과', '배', '복숭아']
i = 0
j = len(fruit)

while i < j:
    for i in range(j):
        if fruit[i] in favorite_fruits:
            print(f"너 정말 {fruit[i]}를 좋아하는구나!")
    i += 1
"""

fruits = ['사과', '배', '복숭아', '수박', '체리']
favorite_fruits = ['사과', '배', '바나나']

for favorite_fruit in favorite_fruits:
    if favorite_fruit in fruits:
        print(f"너는 {favorite_fruit}를 먹으렴!")
    else:
        print(f"{favorite_fruit}는 지금 없는 걸!")