'''
def make_pizza(*toppings):
    """주문받은 토핑 리스트 출력"""
    print("\nMaking a pizza with the fowlling toppings")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
'''
def make_pizza(size, *toppings):
    """만들려고 하는 피자를 요약한다"""
    print(f"\nMaking a {size}-inch pizza with the fowlling toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(16, 'pepperoni')
make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')
'''
'''
def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만든다"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'eistein', loaction='princeton', field='physics')
print(user_profile)
'''

# 연습문제 8-12
def make_sandwitch(*toppings):
    print("요청한 토핑은:")
    for topping in toppings:
        print(f" - {topping}")

make_sandwitch('햄')
make_sandwitch('계란', '치즈', '양상추')

# 연습문제 8-13
def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만든다"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('들깨', '순두부', job='editor', location='seoul')
print(user_profile)

# 연습문제 8-14
def make_car(maker, model, **options):
    """자동차 정보를 저장하는 함수"""
    options['maker_name'] = maker
    options['model_name'] = model
    return options

car = make_car('삼성', 'SM3', wheel='4륜', window='지붕창문')
print(car)