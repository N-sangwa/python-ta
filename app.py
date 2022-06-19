import sys
import os


def prime(number):
    if number >1:
        for x in range(2,number):
            if (number % x) ==0:
                break
        else:
            return f"{x} is not a prime number"
    else: 
        return f"{x} is a prime number"


def solution(number):
    return prime(number)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
