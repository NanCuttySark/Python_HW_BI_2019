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

# example:
a = 1
b = 2
c = 3
# 2.905

# 2) body mass index calculation
mass = int(input("What is your body mass in kg?\n"))
height = float(input("What is your height in meters>\n"))
BMI = mass / height ** 2
print('Your body mass index is', round(BMI, 1))

# example:
mass = 79
height = 1.81
# Your body mass index is 24.1

# 3) The number of combinations from n by k
n = int(input("How many elements are in the set?\n"))
k = int(input("How many elements are taken from the set?\n "))
C_n_k = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print("The number of combinations is", int(C_n_k))

# example
n = 100
k = 8
# The number of combinations is 186087894300

# TO DO: truth tables

# fizzbuzz
number = int(input("Give me the number, please :)"))
if number % 15 == 0:
    print("fizzbuzz")
else:
    if number % 3 == 0:
        print("fizz")
    else:
        if number % 5 == 0:
            print("buzz")

