#files and directories
import os
print(os.getcwd()) #Текущая директория
print(os.listdir())#все файлы и каталоги в pythonProject
path = str(input("Insert path : ")) #'C/Users/zulqa/pythonProject'
if os.path.exists(path): #проверка по директории
    print(True)
else:
    print(False)

print('Exist:', os.access('C\\Users\\zulqa\\pythonProject\\Database.txt', os.F_OK))
print('Readable:', os.access('C\\Users\\zulqa\\pythonProject\\Database.txt', os.R_OK))
print('Writable:', os.access('C\\Users\\zulqa\\pythonProject\\Database.txt', os.W_OK))
print('Executable:', os.access('C\\Users\\zulqa\\pythonProject\\Database.txt', os.X_OK))

with open('Database.txt') as f:
    print(sum(1 for _ in f))

file = open('Database.txt', 'a')
lis = str(input("Insert list : "))
lis1 = list(lis)
lis2 = str(lis1)
file.write(lis2)
file.close()
path1 = str(input("Path : "))
if os.path.exists(path1):
    os.removedirs('files')
else:
    print("Path doesn't exist ! ")



import math

#func
def multip(lis):
    m = 1
    for i in lis:
        m *= i
    print(m)

multip([1, 4, 5, 6, 2])
multip([4,5,4,0])

def check(string):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "abcdefghijklmnopqrstuvwxyz"
    num1 = 0
    num2 = 0
    for i in string:
        if i in a:
            num1 += 1
        else:
            num2 += 1
    print("количество прописных букв: " + str(num1))
    print("количество строчных букв: " + str(num2))

check("Today")
check("")

def checkk(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)

checkk("Gizat")
checkk("ABBA")

def sqrt(number):
    print(math.sqrt(number))

sqrt(25100)


def chegTuple(tup):
    pass