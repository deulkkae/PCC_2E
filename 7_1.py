'''
message = input("Tell me something and I will repeat it bact to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")


prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first name?: "

name = input(prompt)
print(f"\nHello, {name}!")


age = input("How old are you? ")
age = int(age)
age >= 50
'''
'''
height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else: 
    print("\nYou'll be able to ride when you're a little older.")
'''
'''
number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else: 
    print(f"\nThe number {number} is odd.")
'''

# 연습문제
'''
rentcar = input("어떤 차를 원하나요?")
print(f"{rentcar}를 찾아보겠습니다.")

member = input("식사는 몇 명이 하시나요?")
member = int(member)

if member >= 9:
    print("자리가 날 때까지 기다려야 합니다.")
else: 
    print("예약을 완료했습니다. ")
'''

number = input("숫자를 입력하세요: ")
number = int(number)

if number % 10 == 0:
    print("10의 배수가 맞습니다.")
else: 
    print("10의 배수가 아닙니다. ")