import math

try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and logarithm require non-negative numbers.")
    else:
        print(f"\n Calculations for number: {number}")
        print(f"Square root: {math.sqrt(number)}")
        print(f"Natural logarithm (ln): {math.log(number)}")
        print(f"Sine (in radians): {math.sin(number)}")

except ValueError:
    print("Please enter a valid numeric value.")
