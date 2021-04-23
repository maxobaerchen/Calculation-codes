# prime number checker
from math import ceil


def get_number():
    while True:
        enter = input("Enter a number you would like to check for prime:")
        try:
            enter = int(enter)
            return enter
        except ValueError:
            print("This is not a valid input for a natural number")


def round_number(num):
    root = num ** (1/2)
    rounded = ceil(root)
    return rounded


def check_for_prime(num, root):
    for i in range(2, root):
        if num % i == 0:
            return False
        elif i == root - 1:
            return True
        else:
            continue


number = get_number()
rounded_number = round_number(number)

if __name__ == "__main__":
    if check_for_prime(number, rounded_number):
        print("This number is prime! ")
    else:
        print("This number is not prime")