ticket = input()
half_1 = int(ticket[0])+int(ticket[1])+int(ticket[2])
half_2 = int(ticket[3])+int(ticket[4])+int(ticket[5])

if(half_1==half_2):
    print("YES")
else:
    print("NO")
