inp = input().split(" ")
word_1 = inp[0].lower()
word_2 = inp[1].lower()
# Сортируем массивы для дальнейшего сравнения.
word_1 = sorted(word_1)
word_2 = sorted(word_2)

# Спасибо питону за почленное сравнивание.
if word_1 == word_2 :
    print("Yes")
else:
    print("No")
