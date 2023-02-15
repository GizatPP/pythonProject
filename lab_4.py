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