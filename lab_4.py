import datetime
#date
x = datetime.datetime.now()
txt = ""
txt += str(x.year) + " "
txt += str(x.month) + " "
txt += str(x.day - 5)
print(txt)
print(" ")
print("yesterday : " + str(x.day - 1))
print("today : " + str(x.day))
print("tomorrow : " + str(x.day + 1))
print("microsecond : " + str(x.microsecond))
dif = (x.day) - (x.day - 1)
print(dif)
print(dif * 86400)

#generator
n = int(input("Insert number N : "))
s = [i **2 for i in range(1, n)]
print(s)
m = int(input("Insert : "))
x = [i for i in range(1, m) if i % 2 == 0]
print(x)
def gen(c):
    x = [i for i in range(1, c) if i % 3 == 0 or i % 4 == 0]
    print(x)

c = int( input("Insert : "))
gen(c)
a = int(input("Insert a : "))
b = int(input("Insert b : "))
squares = [i **2 for i in range(a, b)]
for j in squares:
    print(j)
n1 = int(input("Insert n1 : "))
g = [i for i in range(0, n1 + 1)]
print(g[::-1])

#math
import math
def conv(degree):
    radian = float(degree * 0.01745329252)
    print("Output degree: " + str(radian) )

degree = float(input("Input degree: "))
conv(degree)
def calc(height, fvalue, svalue):
    area = float(height * ((fvalue + svalue) / 2))
    print("Expected output: " + str(area))

height = float(input("Height: "))
fvalue = float(input("Base, first value: "))
svalue = float(input("Base, second value: "))
calc(height, fvalue, svalue)

def acalc(base, height):
    area = base * height
    print("Expected Output: " + str(area))

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
acalc(base, height)

def f4calc(n_sides, s_length):
    p_area = n_sides * (s_length ** 2) / (4 * math.tan(math.pi / n_sides))
    print("The area of the polygon is: " + str(p_area))

n_sides = float(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
f4calc(n_sides, s_length)
