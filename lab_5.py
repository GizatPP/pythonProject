import re
#Python program to find the sequences of one upper case letter followed by lower case letters.
sentence = str(input("Insert your sentence: "))
if re.findall(r'[A-Z]+[a-z]', sentence):
    print(True)
    res = re.findall(r'[A-Z]+[a-z]', sentence)
    print(res)
else:
    print(False)
print(re.findall(r'[A-Z]+[a-z]', sentence))
#Python program to find sequences of lowercase letters joined with a underscore.
sentence1 = str(input("Insert your sentence: "))
if re.findall(r'[a-z]+[_]', sentence1):
    print(True)
else:
    print(False)
print(re.findall(r'[a-z]_', sentence1))
#Python program to replace all occurrences of space, comma, or dot with a colon.
sentence2 = str(input("Insert your sentence: "))
if re.findall(r',', sentence2):
    print(re.sub(r',', ':', sentence2))

elif re.findall(r' ', sentence2):
    print(re.sub(r' ', ':', sentence2))

elif re.findall(r'.', sentence2):
    for i in range(len(sentence2)):
        if sentence2[i] == '.':
            print(sentence2.replace('.', ':'))
            break
else:
    print(False)
#Python program that matches a string that has an 'a' followed by zero or more 'b''s.
sentence3 = str(input("Insert your sentence : "))
if re.findall(r'(ab*)$', sentence3):
    print(re.findall(r'(ab*)$', sentence3))
else:
    print(False)
#Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
sentence4 = str(input("Insert your sentence : "))
if re.findall(r'(a\w*b)$', sentence4):
    print(re.findall(r'(a\w*b)$', sentence4))
else:
    print(False)
#Python program to insert spaces between words starting with capital letters.
sentence5 = str(input("Insert your sentence : "))
if re.sub(r'(\w)([A-Z])', r'\1 \2', sentence5):
    print(re.sub(r'(\w)([A-Z])', r'\1 \2', sentence5))
else:
    print(False)
#Python program that matches a string that has an 'a' followed by two to three 'b'.
sentence6 = str(input("Insert your sentence : "))
if re.findall(r'(ab{2,3})$', sentence6):
    print(re.findall(r'(ab{2,3})$', sentence6))
else:
    print(False)
#Python program to split a string at uppercase letters.
sentence7 = str(input("Insert sentence : "))
str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', sentence7)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower())
#python program to convert snake case string to camel case string.
sentence8 = str(input("Insert : "))
print(''.join(x.capitalize() or '_' for x in sentence8.split('_')))
#Python program to split a string at uppercase letters.
sentence9 = str(input("Insert : "))
print(re.findall('[A-Z][^A-Z]*', sentence9))