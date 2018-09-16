import math

def isprime(num):
    # first we shoud check if the number is less than 2
    #numbers less than 2 are not prime
    if num < 2:
        return False

    for i in range(2,int(math.sqrt(num))+1):
        if num/i == 0:
            return False
        return True


number = input("Enter the number to find out if it is prime or not")
if isprime(int(number)):
    print("The number %s is prime number" %number)
else:
    print("the number %s is not prime" %number)