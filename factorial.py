def factorial(num):
    for i in range(1,num):
        num *= i
    return num


def factorial_recursive(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursive(num - 1)

print(factorial(8))
print(factorial_recursive(8))

