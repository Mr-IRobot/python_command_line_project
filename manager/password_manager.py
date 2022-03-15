from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open ('key.key', 'wb') as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    file = open ('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_password = input("Enter a master password | ")
master = (master_password)

key = load_key() + master_password.encode()
fer = Fernet(key)


def view():
    with open ('password.txt', 'r') as file:
        for line in file.readlines():
            data = (line.rstrip())
            user, passw = data.split('|', '|')
            print ('username: ', user, '| password: ', fer.decrypt(passw.encode()).decode())

def add():
    username = input("Input your username | ")
    password = input("Input your password | ")

    with open ('password.txt', 'a') as file:
        file.write(username +' | '+ fer.encrypt(password.encode()).decode() +'\n')
        #file.write('Username = ' + username +' | Password = ' + password +'\n')

while True:
    mode = input("Would you like to add a new password or view the existing password (view, add)? OR press Q to quit | ").lower()
   
    if mode == "q":
        print ("Process ended")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print ("Invalid input, Pls try again") 
        continue

    
    
        

