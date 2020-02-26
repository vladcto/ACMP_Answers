inp = input().split(" ")
W = int(inp[0])
H = int(inp[1])
# Диаметр = 2 * радиус
D = int(inp[2]) * 2

if D <= W and D <= H:
    print("YES")
else:
    print("NO")
