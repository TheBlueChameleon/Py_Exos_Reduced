# ============================================================================ #
# Problem 1

number = float(input("Bitte geben Sie eine Zahl ein: "))
print(2 * number)

# ============================================================================ #
# Problem 2

print(f"{22/7:5.3f}")

# Funny side note: The value 22/7 is sometimes cited as a "good approximation
# for pi"
# At least in engineering context, this is sometimes really used. Also, 22 July
# is sometimes celebrated as "alternative pi day" for that reason, (next to
# March 14, of course)

# ============================================================================ #
# Problem 3

x = float(input("Please provide a number: "))

if x**2 - 49 == 0 :
    print("Your input is a solution to x^2 - 49")
else:
    print("Your input is no solution to x^2 - 49")

# ============================================================================ #
# Problem 4

year = int(input("Please provide a year: "))

if         year %   4 == 0 :
    if     year % 100 == 0 :
        if year % 400 == 0 :
            print("leap year")
        else :
            print("no leap year")
    else :
        print("leap year")
else :
    print("no leap year")


# Alternativ auch:

if (year % 400 == 0 or (year % 4 == 0  and year % 100 != 0)) :
    print("ist leap year")
else :
    print("ist no leap year")

# oder

leapYear = False
if   year % 400 == 0 :
  leapYear = True
elif year % 100 == 0 :
  leapYear = False
elif year %   4 == 0 :
  leapYear = True
else :
  leapYear = False

print(f"The year {year} is", "a" if leapYear else "no", "leap year")

# ============================================================================ #
# Problem 5

import math
import cmath

print("REAL VALUED TREATMENT:")

aStr = input("Please provide a number a:")
bStr = input("Please provide a number b:")
cStr = input("Please provide a number c:")

a = float(aStr)
b = float(bStr)
c = float(cStr)

discr = b**2 - 4 * a * c

if discr == 0 :
    x = -b / (2*a)
    print("There's one solution: x =", x)

elif discr > 0 :
    x_1 = (-b + math.sqrt(discr)) / (2*a)
    x_2 = (-b - math.sqrt(discr)) / (2*a)

    print("There are two solutions:")
    print("  x_1 =", x_1)
    print("  x_2 =", x_2)

else :
    print("There's no solution!")


# since now complex coefficients are possible, ask to re-enter them
print("COMPLEX VALUED TREATMENT:")

aStr = input("Please provide a number a:")
bStr = input("Please provide a number b:")
cStr = input("Please provide a number c:")

a = complex(aStr)
b = complex(bStr)
c = complex(cStr)

discr = b**2 - 4 * a * c

if discr == 0 :
    x = -b / (2*a)
    print("There's one solution: x =", x)

else :
    x_1 = (-b + cmath.sqrt(discr)) / (2*a)
    x_2 = (-b - cmath.sqrt(discr)) / (2*a)
    
    print("There are two solutions:")
    print("  x_1 =", x_1)
    print("  x_2 =", x_2)
