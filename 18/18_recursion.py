def factorial(_number):
    if _number <=1:
        return 1
    else:
        return factorial(_number-1)*_number

number = int(input())
print(factorial(number))
