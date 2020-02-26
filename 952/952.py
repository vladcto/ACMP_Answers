inp = input().split(" ")
adult = int(inp[0])
child = int(inp[1])

if adult == 0 and child == 0:
    print("0 0")
    quit()

if adult == 0:
    print("Impossible")
    quit()

min = 0
# К каждому взрослому один бесплатный ребенок =>
# "Платные дети" это разница между взрослыми и всеми детьми
not_free_child = child - adult
# Если детей было меньше, то может оказаться отриц. ответ
if not_free_child < 0:
    not_free_child = 0
min = adult + not_free_child

max = 0
# К одному взрослому приписывает всех детей,
# кроме одного "бесплатного".
if child == 0:
    # Если нет детей, то не нужно и отнимать "бесплатного"
    max = adult
else:
    max = adult + child - 1

print("{} {}".format(min, max))
