"""
# 이름만 반복
players = ['나리', '다빈', '다정', '병산', '해북']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

# 한 줄씩 반복
players = ['나리', '다빈', '다정', '병산', '해북']

for player in players[:3]:
    print(f"Here is the players on my team: {player}")

# 리스트 복사하기
my_foods = ['피자', '햄버거', '커피', '라면']
his_foods = my_foods[:]

my_foods.append('케이크')
his_foods.append('아이스크림')

print(my_foods)
print(his_foods)
"""

# 연습문제
players = ['나리', '다빈', '다정', '병산', '해북']
print(f"리스트의 첫 세 항목은 {players[:3]} 이다.")
print(f"리스트의 중간 세 항목은 {players[1:4]} 이다.")
print(f"리스트의 마지막 세 항목은 {players[-3:]} 이다.")

pizza = ['페퍼로니', '하와이언', '불고기']
friend_pizza = pizza[:]

pizza.append('슈퍼슈프림')
friend_pizza.append('핫불고기')

print("내가 좋아하는 피자는: ")
print(pizza)
print("친구가 좋아하는 피자는: ")
print(friend_pizza)