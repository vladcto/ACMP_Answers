inp = input().split(" ")
C = int(inp[0])
H = int(inp[1])
O = int(inp[2])

#Определяю на сколько молекул хватит этих веществ.
C_enough = C // 2
H_enough = H // 6
O_enough = O

print(min(C_enough, H_enough, O_enough))
