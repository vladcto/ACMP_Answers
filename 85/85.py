# Алгоритм Евклида
# Спасибо Python за большую арифметику
input_string = input().split(" ")
a = int("1" * int(input_string[0]))
b = int("1" * int(input_string[1]))

if a > b:
    while True:
        tmp = a % b
        a = b
        b = tmp
        if b == 0:
            print(a)
            break
else:
    while True:
        tmp = b % a
        b = a
        a = tmp
        if a == 0:
            print(b)
            break
