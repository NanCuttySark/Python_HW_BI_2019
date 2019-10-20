import math

# conversions from integers to fractions
float(5)
float(6)
float(-879867)
float(10)
float(90776)

# from fractions to integers
int(3 / 4)
int(10.0)
int(6 / 3)
int(3.141592653589793238462643)
int(-456.0986)

# from int to string
str(5)
str(int(4 / 7))
str(98652)
str(8765)
str(int(math.pi))

# from float to string
str(65.098)
str(math.pi)
str(3 / 14)
str(float(5))
str(-76.763210964)

# from string to int (I hope I got the task correctly)
int(str(5))
int(float(str(98 / 76)))
int('5')
int('98975')
int('-98975')

# from string to float
float('5')
float('-87664.347')
float(str(7))
float(str(3 / 14))
float(str(math.pi))

# formulas
# 1) triangle area on three sides
a = int(input("длина стороны треугольника:\n"))
b = int(input("длина другой стороны треугольника:\n"))
c = int(input("длина другой стороны треугольника:\n"))
half_perimeter = 0.5 * (a + b + c)
triangle_area = (half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)) ** 0.5
print(round(triangle_area, 3))

"""
example:
a = 1
b = 2
c = 3
2.905
"""

# 2) body mass index calculation
mass = int(input("What is your body mass in kg?\n"))
height = float(input("What is your height in meters>\n"))
BMI = mass / height ** 2
print('Your body mass index is', round(BMI, 1))

"""
example:
mass = 79
height = 1.81
Your body mass index is 24.1
"""

# 3) The number of combinations from n by k
n = int(input("How many elements are in the set?\n"))
k = int(input("How many elements are taken from the set?\n "))
C_n_k = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print("The number of combinations is", int(C_n_k))

"""
example
n = 100
k = 8
The number of combinations is 186087894300
"""

# truth table for NOT
def f(i):
    return not i


def main():
    print("not  x   | result ")
    print("---------+--------")
    for i in [True, False]:
        print("not", i, "|", f(i))


main()
"""
 красиво не получилось, не знаю, как внести поправку на разную длину слов True и False
 output: 
not  x   | result 
---------+--------
not True | False
not False | True
"""
# truth table for OR
def g(x, y):
    return x or y


def main():
    print("  x  or   y   | result ")
    print("--------------+--------")
    for x in [True, False]:
        for y in [True, False]:
            print(x, "or", y, "|", g(x, y))


main()
"""
output:
  x  or   y   | result 
--------------+--------
True or True | True
True or False | True
False or True | True
False or False | False
"""
# truth table for XOR
def t(q, w):
    return q ^ w


def main():
    print("  x   ^   y   | result ")
    print("--------------+--------")
    for q in [True, False]:
        for w in [True, False]:
            print(q, " ^ ", w, "|", t(q, w))


main()
"""
  x   ^   y   | result 
--------------+--------
True  ^  True | False
True  ^  False | True
False  ^  True | True
False  ^  False | False
"""
# truth table for NOR
def p(aa, bb):
    return not (aa or bb)


def main():
    print("  x  nor   y   | result ")
    print("---------------+--------")
    for aa in [True, False]:
        for bb in [True, False]:
            print(aa, "nor", bb, "|", p(aa, bb))


main()
"""
  x  nor   y   | result 
---------------+--------
True nor True | False
True nor False | False
False nor True | False
False nor False | True
"""
# truth table for AND
def u(qq, tt):
    return qq and tt


def main():
    print("  x  and   y   | result ")
    print("---------------+--------")
    for qq in [True, False]:
        for tt in [True, False]:
            print(qq, "and", tt, "|", u(qq, tt))


main()
"""
  x  and   y   | result 
---------------+--------
True and True | True
True and False | False
False and True | False
False and False | False
"""
# truth table for NAND
def p(xx, yy):
    return not (xx and yy)


def main():
    print("  x  nand   y  | result ")
    print("---------------+--------")
    for xx in [True, False]:
        for yy in [True, False]:
            print(xx, "nand", yy, "|", p(xx, yy))


main()
"""
  x  nand   y  | result 
---------------+--------
True nand True | False
True nand False | True
False nand True | True
False nand False | True
"""

# fizzbuzz
number = int(input("Give me the number, please :)"))
if number % 15 == 0:
    print("fizzbuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")

