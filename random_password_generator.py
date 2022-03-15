import random


print ('Welcome! TO Your Password Generator')

chars = ('ABCDEFGHIJKLMNOPQRSTUVWSYZabcdefghijklmnopqrstuvwsyz0123456789!@#$%^&*()')

amount = input('Enter the amount of passwords to generate : ')
amt = int(amount)

lenght = input('Enter your desired lenght of the password to generate : ')
len = int(lenght)

print ('\nHere are your random passwords : ')

for pwd in range(amt):
    passwords = ''
    for pwdd in range(len):
        passwords += random.choice(chars)
    print (passwords)

