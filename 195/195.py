string = input().split(" ")
number=[int(string[0]),int(string[1]),int(string[2])]
# S одной панели = a*b
# S всей поверхности = a*b*n
# С двеух сторон поэтому ansewr = 2*S_все_поверх.
print(number[0]*number[1]*number[2]*2)
