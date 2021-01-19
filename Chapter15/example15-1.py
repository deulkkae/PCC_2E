# 연습문제 15-1

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#차트 제목과 축 라벨을 정하자
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)

#눈금 라벨 크기를 정하자
ax.tick_params(axis='both', which='major', labelsize=14)

#각 축의 범위를 정하자
ax.axis([0, 5000, 0, 125000000000])

plt.show()
