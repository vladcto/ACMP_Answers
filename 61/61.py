score = 0 # Перевес очков в какую-то команду
for i in range(0,4):
    inp = input().split(" ")
    score+=int(inp[0])
    score-=int(inp[1])
if score==0:
    print("DRAW")
else:
    if score>0:
        print(1)
    else:
        print(2)
