"""
requested_toppings = ['버섯', '피망', '치즈']

for requested_topping in requested_toppings:
    if requested_topping == '피망':
        print("지금 그거 없다")
    else: 
        print(f"{requested_topping}을 추가하세요!")

print("\n피자 만들기 끝!")


requested_toppings = []

if requested_toppings: # 파이썬에서 리스트 이름을 if 문에 사용하면, 리스트 항목에 최소한 하나 이상 있을 때 True를 반환한다.
    for requested_topping in requested_toppings:
        print(f"{requested_topping}을 추가하세요!")
    print("\n피자 만들기 끝!")

else: 
    print("진짜 토핑 없어?")

available_toppings = ['버섯', '올리브', '파인애플', '치즈', '피망']
requested_toppings = ['버섯', '피망', '치즈', '가지']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"{requested_topping}을 넣어주세요!")
    else:
        print(f"{requested_topping}은 지금 없어요.")
"""

# 연습문제
users = ['olive', 'david', 'nari', 'admin']
if users:
    for user in users:
        if user == 'admin':
            print("관리자님 안녕하세요. 상태 보고서를 보시겠습니까?")
        else:
            print(f"{user}님, 다시 로그인해주셔서 감사합니다.")
else:
    print("사용자가 있어야 합니다!")

current_users = ['olive', 'david', 'nari', 'admin', 'dave']
new_users = ['dave', 'bbb', 'ccc', 'nari', 'eee']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user}는 이미 사용 중인 아이디입니다.")
    else: 
        print(f"{new_user}는 사용할 수 있는 아이디입니다.")

numbers = list(range(1, 10))
print(numbers)
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif 2 <= number <= 3:
        print(f"{number}nd")
    else: 
        print(f"{number}th")
    