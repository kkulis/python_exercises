

numbers_list = [var for var in range(1,101)]

print(numbers_list)


for number in numbers_list:
    if number % 3 == 0:
        print("fizz")
    if number % 5 == 0:
        print("buzz")
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuZZ")
    else:
        print(number)

