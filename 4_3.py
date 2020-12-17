"""
# range()로 숫자 범위 만들기
for value in range(1, 5):
    print(value)

# list()로 숫자 리스트 만들기
numbers = list(range(1,6))
print(numbers)

# 짝수만 출력
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 홀수만 출력
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

# 제곱수 출력
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# 숫자 리스트를 이용한 단순한 통계
digits = list(range(0, 10))
print(min(digits))
print(max(digits))
print(sum(digits))

# 리스트 내포(list comprehension)
squares2 = [value**2 for value in range(1, 11)]
print(squares2) 
"""

# 연습문제
for value in range(1, 21):
    print(value)

for value2 in range(1, 100):
    print(value2)

digits = list(range(1, 1000001))
print(min(digits))
print(max(digits))
print(sum(digits))

odd_list = list(range(1, 20, 2))
print(odd_list)

for cube in range(1, 11):
    print(cube**3)

cubes = [value**3 for value in range(1, 11)]
print(cubes)