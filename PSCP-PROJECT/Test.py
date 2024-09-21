import string
import random
"""choose"""
char = ''
letters = False
digits = False
punctuation = False
lenght = int(input('How long? '))
l = input('Do you want letters: ')#จริงๆก็เป็นการติ้กแหละ
d = input('Do you want digits: ')#
p = input('Do you want punctuation: ')#
if l =='Yes':
    letters = True

if letters == True:#กดติ้ก
    only_lower = 0
    only_upper = 0
    up = input('Letters Up? ')
    lo = input('Letters Lower? ')
    if up == '1':#กดติ้ก
        only_upper+=1
        char+=string.ascii_uppercase
    elif up == '0':#ไม่กดติ้ก
        char = ''
    
    if lo == '1':#กดติ้ก
        only_lower+=1
        char+=string.ascii_lowercase
    elif lo == '0':#ไม่กดติ้ก
        char = ''

if d == 'Yes':#กดติ้ก
    digits = True
    
if digits == True:
    char+=string.digits

if p == 'Yes':
    punctuation = True

if punctuation == True:
    char+=string.punctuation
    
password = []
for i in range(lenght):
    randoms = random.choice(char)
    password.append(randoms)
print(''.join(password))