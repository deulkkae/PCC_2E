'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
'''
'''
prompt = "\nTell me something and I will repeat it bact to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else: 
        print(message)
'''
'''
prompt = "Please enter the name of a city you have visited.: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else: 
        print(f"I'd love to go to {city.title()}!")
'''
'''
current_number = 0 
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
'''

# 연습문제
'''
prompt = "토핑을 입력하세요."
prompt += "\n'다 넣었다!'를 입력하면 토핑 넣기가 종료됩니다.: "
topping = ""

while True:
    topping = input(prompt)
    
    if topping == '다 넣었다!':
        break
    else: 
        print(f"{topping}을 넣었습니다.")
'''

# 연습문제 7-5
'''
prompt = "나이를 입력하세요"
prompt += "\n(종료하고 싶으면 아무 문자나 입력하세요.): "
age = input(prompt)

active = True
while active:
    if age.isdigit():
        age2 = int(age)
        if 0 <age2 <3:
            print("무료입니다. ")
        elif 3 <= age2 <= 12:
            print("$10")
        elif age2 > 12:
            print("$15")
    elif age.isalpha():
        print("프로그램을 종료합니다.")
        # active = False  
'''

