inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
d = int(inp[3])
root = []

for i in range(-100, 101):
    if a * i ** 3 + b * i ** 2 + c * i + d == 0:
        root.append(str(i))
print(" ".join(root))
