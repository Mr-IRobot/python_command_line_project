from ast import IsNot
from operator import is_not
from tkinter import MULTIPLE
from tokenize import Double


#s = ['(',')','[',']','{','}']
s = ['(',')','[',']','{','}','()','[]','{}','()[]','(){}','[]()','[]{}','{}()','{}[]','()[]{}','[](){}','{}[]()','()()','[][]','{}{}','()()()','[][][]','{}{}{}']

char = input("Enter symbol: ")

if char not in s:
    print('Pls a character')
else:
    while True:
        if char == '(' + ')':
            print(char)
            print('correct!')
        elif char == '[' + ']':
            print(char)
            print('correct!')
        elif char == '{' + '}':
            print(char)
            print('correct!')
        elif char == '()' + '[]':
            print(char)
            print(' bracket')
        elif char == '()' + '[]' + '{}':
            print(char)
            print('Bbracket')
        elif char == '(' or ')':
            print(char)
            print('Incomplete bracket')
        else:
            print('Incorrect combination')
        break