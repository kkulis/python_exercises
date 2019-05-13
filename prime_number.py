
num = int(input("give number: "))

def is_Prime(num):
    if num > 1:

        for i in range (2,num):
            if num % i == 0:
                print("is not prime number")
                break
        else:
            print("is prime number")

#http://lichota.pl/python_dev_interview_012018.pdf
