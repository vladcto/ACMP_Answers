import math

inp = input().split(" ")
H = int(inp[0])
A = int(inp[1])
B = int(inp[2])

# Когда улитка доходит до конца, она перед этим один раз проходит дистанцию A.
H = H - A
days = 1

#Проверяем , что если улитка в первый день уже прошла
if H > 0:
    # Округляеем в большую, так как улитка проходит фиксированные дистанции
    days = days + math.ceil( H / (A - B))
print(days)
