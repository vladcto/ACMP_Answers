a = int(input())
n = abs(a - 2) if a <= 0 else a
sum = int( n * (1 + a) / 2)
print(sum)
