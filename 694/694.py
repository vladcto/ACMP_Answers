# я нахожу такой период времени в котором каждый преподователь
# мог бы работать.
n = int(input())
# Максимальный начальный день для работы одного из преподователей
start_day = 0
# Минимальный конечный день работы для рабоыт одного из преподователей
end_day = 32

for i in range(0,n):
    inp = input().split(" ")
    a = int(inp[0])
    b = int(inp[1])

    # Проверка , что распиание точно не входит в расписания других.
    if a > end_day or b < start_day:
        print("NO")
        quit()
    else:
        if a > start_day:
            start_day = a
        if b < end_day:
            end_day = b
print("YES")
