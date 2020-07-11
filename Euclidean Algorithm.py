
#-------------------------------------------------------------------------------
# Name:        Caesar Cipher
#
# Author:      Rishabh Acharya
#
# Created:     10-07-2020
#-------------------------------------------------------------------------------

def ext_euclid(a, b):
    a, b = abs(a), abs(b)
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def main():

    while True:
        try:
            a = int(input("Insert the first number (must be integer): "))
            b = int(input("Insert the second number (must be integer): "))
            break
        except ValueError:
            print("\nYou must enter two numbers!\n")

    gcd, x, y = ext_euclid(a, b)
    print("\nGreatest Common Divisor (GCD):", gcd)

if __name__ == '__main__':
    main()