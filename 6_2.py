'''
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 외계인을 오른쪽으로 움직인다.
# 외계인의 현재 속도를 통해 얼마나 많이 움직일지 결정한다.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 빠른 외계인
    x_increment = 3

# 새 위치는 이전 위치에 x_increment를 더한 값
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color':'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
'''

# 연습문제
people = {
    'first_name': '나리',
    'last_name': '윤',
    'age': 32,
    'city': 'Seoul'
}
print(people)

favorite_number = {
    '다빈' : 1,
    '나리' : 3,
    '다정' : 7,
    '병산' : 2,
    '해북' : 11
}
number1 = favorite_number['다빈']
number2 = favorite_number['나리']
number3 = favorite_number['다정']
number4 = favorite_number['병산']
number5 = favorite_number['해북']
print(f"다빈이가 가장 좋아하는 숫자는 {number1}.")
print(f"나리가 가장 좋아하는 숫자는 {number2}.")
print(f"다정이가 가장 좋아하는 숫자는 {number3}.")
print(f"병산이가 가장 좋아하는 숫자는 {number4}.")
print(f"해북이가 가장 좋아하는 숫자는 {number5}.")
