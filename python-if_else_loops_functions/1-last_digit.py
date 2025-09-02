#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(number):
    if number < 0:
        return -(abs(number) % 10)
    else:
        return number % 10
    

if last_digit(number) > 5:
    print(
        f"Last digit of {number} is {last_digit(number)} "
        "and is greater than 5"
    )
elif last_digit(number) == 0:
    print(f"Last digit of {number} is {last_digit(number)} and is 0")
elif last_digit(number) < 6 and last_digit(number) != 0:
    print(
        f"Last digit of {number} is {last_digit(number)} "
        "and is less than 6 and not 0"
    )
