max = int(input())
days = input().split(" ")
# Четные - четверки
even = []
# Нечетные - тройки
uneven = []

for number in range(0, max):
    day = days[number]
    if int(day) % 2 == 0:
        even.append(day)
    else:
        uneven.append(day)

print(" ".join(uneven))
print(" ".join(even))
print("YES" if not len(even) < len(uneven) else "NO")
