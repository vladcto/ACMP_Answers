# Также можно решить через арифмитиечскую прогрессию
# В этой задачи могут быть отрицательные входные данные
# Поэтому пришлось делать проверку.

answer = 0
max_number = int(input())
step = 1
if max_number <= 0:
    step = -1
for number in range(1, max_number + step, step):
    answer += number
print(answer)
