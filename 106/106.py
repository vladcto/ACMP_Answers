n = int(input())
# Для того , что бы все монеты были одинаковы нам надо:
# Либо перевернуть все решко.
# Либо перевернуть все орлы.
flip_0 = 0
flip_1 = 0
for i in range(0,n):
    type_money = int(input())
    if type_money == 0:
        # Переворачиваем решкой вверх.
        flip_0=flip_0+1
    else:
        # Переворачиваем орлом вверх.
        flip_1 = flip_1 + 1
print(min(flip_0,flip_1))
