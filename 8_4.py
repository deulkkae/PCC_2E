'''
def greet_users(names):
    """리스트의 각 사용자에게 단순한 환영 인사를 출력한다"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
'''
'''
# 출력할 디자인
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 게 없을 때까지 디자인의 출력을 시뮬레이트
# 출력한 각 디자인을 completed_models로 옮긴다

while unprinted_designs:
    current_design = unprinted_designs.pop()

    print(f"Printing Model: {current_design}")
    completed_models.append(current_design)

# 출력이 끝난 모델 모두 표시
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
'''
'''
def print_models(unprinted_designs, completed_models):
    """남은 게 없을 때까지 디자인의 출력을 시뮬레이트
    출력한 각 디자인을 completed_models로 옮긴다"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """출력이 끝난 모델 모두 표시"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)
'''
# 연습문제
'''
def show_magicians(names):
    """마술사 이름을 출력하자"""
    for name in names:
        print(name)
'''

'''
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

list_a = list_b

print(list_a)
'''

# 연습문제 8-10
def show_magicians(names):
    """마술사 이름을 출력하자"""
    print(names)

def make_great(magicians, great_magicians):
    """리스트에 great을 넣어서 수정하자"""
    while magicians:
        popped_magician = magicians.pop()
        edited_magician = f"great {popped_magician}"
        great_magicians.append(edited_magician)
    magicians = great_magicians
    
magicians = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
great_magicians = []

make_great(magicians, great_magicians)
print(magicians)

# 연습문제 8-10 / 8-11
def show_magicians(names):
    """마술사 이름을 출력하자"""
    print(names)

def make_great(names):
    """리스트에 great을 넣어서 수정하자"""
    i = 0
    j = len(names)
    while i < j:
        names[i] = f"great {names[i]}"
        i += 1
    great_magicians = names[:] 
    
magicians = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
great_magicinas = []

make_great(magicians) # 리스트의 사본으로 실행
show_magicians(magicians)
show_magicians(great_magicians)
