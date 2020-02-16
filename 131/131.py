max_age = 0
number_old = -1
last = int(input())

for number_people in range(1, last + 1):
    inp = input().split()
    age = int(inp[0])
    gender = int(inp[1])
    if gender == 1:
        if age > max_age:
            max_age = age
            number_old = number_people

print(number_old)
