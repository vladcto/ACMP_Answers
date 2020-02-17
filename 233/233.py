max = int(input())
bridges_height = input().split(" ")
# Перемен. для высчитвания высота моста относительно прошлого.
last_bridge_height = 0

for i in range(1, max + 1):
    bridge_height = int(bridges_height[i - 1]) - last_bridge_height
    if bridge_height <= 437:
        print("Crash {}".format(i))
        exit()
print("No crash")
