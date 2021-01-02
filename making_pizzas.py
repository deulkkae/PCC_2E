'''
import pizza

pizza.make_pizza(16, '페퍼로니')
pizza.make_pizza(12, '버섯', '초록 피망', '치즈 추가')

# 별칭을 쓰면 이렇게
import pizza as p

p.make_pizza(16, '페퍼로니')
p.make_pizza(12, '버섯', '초록 피망', '치즈 추가')
'''

# 모듈 안에 함수가 여러 개라면 이렇게
# from pizza import make_pizza
from pizza import make_pizza as mp

mp(16, '페퍼로니')
mp(12, '버섯', '초록 피망', '치즈 추가')