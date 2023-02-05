def g_to_o(grams):
    grams = float(grams)
    converter = float(grams * 0.0352739619)
    print(converter)

g_to_o(4)

def convertcel(F):
    cel = float((5 * F - 5 * 32) / 9)
    print(cel)
convertcel(100.12)

def filter_prime(nums):
    for i in nums:
        if i % 2 == 1:
            print(i)

nums = [1,2,4,5,7,9,11]
filter_prime(nums)


def printperm(string):
    if len(string) == 1:
        return [string]
    perms = printperm(string[1:])
    char = string[0]
    res = []
    for i in perms:
        for j in range(len(i) + 1):
            res.append(i[:j] + char + i[j:])

    return res

print(printperm("abc"))

def reverse(word):
    print(word[::-1])

reverse("we are studying")

def check(list):
    for i in range(len(list) - 1):
        if list[i] == 3 and list[i + 1] == 3:
            return True
    return False


list1 = [3,1,2,5]
b = check(list1)
print(b)

def spy_game(nums):
    lis = []
    for i in nums:
        if i == 0 or i == 7:
            lis.append(i)

    for i in lis:
        if lis == [0, 0, 7]:
            print(True)
            break
        else:
            print(False)
            break

spy_game([1,2,4,0,0,7,5])
spy_game([1,7,2,0,4,5,0])

def findv(r):
    pi = 3.1415926535
    print(4/3 * pi * (r * r * r))

findv(1)
findv(23)

def findunique(nums):
    nums = []
    nums.count()