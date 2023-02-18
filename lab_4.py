import datetime

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
