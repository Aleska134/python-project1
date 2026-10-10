# Student Name: Aleska Braschi
# Date: 10/10/2026
# Program Name: Project 1
# Description: Program to calculate the mathematical functions of power, e^x, and sine.
import math

PI = 3.1416          
MAX_TERMS = 50
OUTPUT_FILE = "output.txt"

def save_and_print(text):
    print(text)
    with open(OUTPUT_FILE, "a") as file:
        file.write(text + "\n")

def get_int(input_text):
    while True:
        try:
            return int(input(input_text))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_num_terms():
    while True:
        n = get_int("Enter the number of terms: ")
        if 1 <= n <= MAX_TERMS:
            return n
        print(f"The number of terms must be between 1 and {MAX_TERMS}.")

def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result   # raises ZeroDivisionError if base is 0
    return result


def exponential(x, num_of_terms):
    result = 0
    for n in range(num_of_terms):
        term = power(x, n) / math.factorial(n)
        result += term
        save_and_print(f"n = {n} term is {term:.6f}")
    return result


def sine(x, num_of_terms):
    result = 0
    x_radians = x * PI / 180
    for n in range(num_of_terms):
        term = power(-1, n) * power(x_radians, 2 * n + 1) / math.factorial(2 * n + 1)
        result += term
        save_and_print(f"n = {n} term is {term:.6f}")
    return result


def main():
    option = 0
    while option != 4:
        print("\nMenu of Options:")
        print("1. Power Function")
        print("2. e ^ x")
        print("3. Sine")
        print("4. Quit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            option = 0
            print("Invalid choice. Try again.")
            continue

        try:
            if option == 1:
                base = get_int("Enter the base: ")
                exponent = get_int("Enter the exponent: ")
                result = power(base, exponent)
                save_and_print(f"The result of {base}^{exponent} = {result}")

            elif option == 2:
                x = get_int("Enter the exponent: ")
                num_of_terms = get_num_terms()
                result = exponential(x, num_of_terms)
                save_and_print(f"The result of e^{x} = {result:.6f}")

            elif option == 3:
                x = get_int("Enter the value of x: ")
                num_of_terms = get_num_terms()
                result = sine(x, num_of_terms)
                save_and_print(f"The result of sin({x}) = {result:.6f}")

            elif option == 4:
                print("Exiting the program.")

            else:
                print("Invalid choice. Try again.")

        except ArithmeticError:
            print("Math error: that calculation is undefined or too large. Try different values.")


if __name__ == "__main__":
    main()


