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