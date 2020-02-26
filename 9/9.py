max = int(input())
inp = input().split(" ")
number_array = []

max_number = -1000
min_number = 1000
max_index = 0
min_index = 0
sum = 0

for i in range(0, max):
    number = int(inp[i])
    number_array.append(number)
    if number > 0:
        sum = sum + number

    if number > max_number:
        max_number = number
        max_index = i

    if number < min_number:
        min_number = number
        min_index = i

if max_index < min_index:
    tmp = max_index
    max_index = min_index
    min_index = tmp

product_of_numbers = 1
for number in number_array[min_index + 1:max_index]:
    product_of_numbers = product_of_numbers * number

print("{} {}".format(sum, product_of_numbers))
