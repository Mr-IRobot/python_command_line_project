from ast import Or
from audioop import add
import numbers
from re import T
import re
from tkinter import END, NUMERIC
from tokenize import Number
from unicodedata import numeric
from unittest import result
from xml.etree.ElementPath import ops

'''

def calPoints(ops) -> int:
    result = None

    #my code 

    result = 0
    #record = [5,2]
    record = [5,2,]
    #num = 2
    #n = str(num)

    #while True:

    for op in ops:

        
        
            print (record)
            #if op == numeric(n):
            if line == str(2):
                #record.append(int(op))
                record.append(int(2))
            if line == str(5):
                #record.append(int(op))
                record.append(int(5))
            if line == "C" or "c":
                record.pop()
                print (record)
            if line == "D" or "d":
                record.append(record[-1]*2)
                print (record)
            if line == "+":
                record.append(record[-1] + record[-2])
                print (record)
            
        
        

        
            for result in range(len(record)):
                result = (result + record[0] + record[1] + record[2])
                #result = result + record[i]
                #print (record)
                #print (calPoints([record,"C","D","+"]))
                
                return result
            
                
            
     

        
while True:
    if __name__ == '__main__':
        line = input("Input command: ")
        ops = line.strip().split()
        print(calPoints(ops))
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

'''
    



def calPoints(ops) -> int:
    result = None
    result = 0
    record = [5,2]

    for op in ops:
        while True:   
            print (record) 
            #if op == numeric(n):
            if op == int:
                #record.append(int(op))
                record.append(record)
            if op == numeric:
                #record.append(int(op))
                record.append(record)
            if op == "C" or "c":
                record.pop()
                print (record)
            if op == "D" or "d":
                record.append(record[-1]*2)
                print (record)
            if op == "+":
                record.append(record[-1] + record[-2])
                print (record)
            break
    for i in range(len(record)):
        #result = (result + record[0] + record[1] + record[2])
        result = result + record[i]
    return result
  
if __name__ == '__main__':
    line = input("Input command: ")
    ops = line.strip().split()
    print(calPoints(ops))
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>')



    