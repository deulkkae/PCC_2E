'''
# 확인해야 하는 사용자 리스트, 
# 확인된 사용자를 저장할 빈 리스트로 시작한다
unconfirmed_users = ['alice', 'brain', 'Candace']
confirmed_users = []

# 확인되지 않은 사용자가 더는 없을 때까지 각 사용자를 확인한다
# 확인된 사용자는 확인된 사용자 리스트로 옮긴다
while unconfirmed_users: 
    current_user = unconfirmed_users.pop()

    print(f"Verifing user: {current_user.title()}")
    confirmed_users.append(current_user)

#확인된 사용자를 모두 표시한다
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''
'''
responses = {}

# 설문이 활성화됐다는 플래그를 설정

polling_active = True

while polling_active:
    # 이름과 응답을 물어본다
    name = input("\n이름이 뭐니? ")
    response = input("어떤 산을 좋아하니? ")

    # 응답을 딕셔너리에 저장
    responses[name] = response

    # 다른 사람도 설문에 참여할지 물어보기
    repeat = input("다른 사람도 설문에 참여하게 하시겠습니까? (yes/no)")
    if repeat == 'no':
        polling_active = False

# 설문 끝. 결과를 출력한다. 
print("\n---설문 종료---")
for name, response in responses.items():
    print(f"{name}은 {response} 산을 좋아해.")
'''
'''
# 연습문제
sandwitch_orders = ['햄', '패스트라미', '치즈', '패스트라미', '베이컨', '계란', '패스트라미']
finished_sandwitches = []
print("패스트라미가 다 떨어졌다.")

while '패스트라미' in sandwitch_orders:
    sandwitch_orders.remove('패스트라미')

while sandwitch_orders:
    finished_sandwitch = sandwitch_orders.pop()
    
    print(f"{finished_sandwitch} 샌드위치를 만들었습니다. ")
    finished_sandwitches.append(finished_sandwitch)

print(f"완성한 샌드위치!: {finished_sandwitches}")
'''
# 연습문제 응용
sandwitch_orders = ['햄', '패스트라미', '치즈', '패스트라미', '베이컨', '계란', '패스트라미']
finished_sandwitches = []
print("패스트라미가 다 떨어졌다. 패스트라미 주문은 취소한다!")

while sandwitch_orders:
    finished_sandwitch = sandwitch_orders.pop()
    if finished_sandwitch == '패스트라미':
        print(f"{finished_sandwitch} 주문은 취소합니다.")
    else:     
        print(f"{finished_sandwitch} 샌드위치를 만들었습니다. ")
        finished_sandwitches.append(finished_sandwitch)

print(f"완성한 샌드위치!: {finished_sandwitches}")


