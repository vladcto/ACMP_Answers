inp = input().split(" ")
numbers = []
for i in range(3):
    numbers.append(int(inp[i]))

if numbers[0] + numbers[1] == numbers[2] \
        or numbers[2] + numbers[0] == numbers[1] \
        or numbers[1] + numbers[2] == numbers[0]:
    print("YES")
else:
    print("NO")
