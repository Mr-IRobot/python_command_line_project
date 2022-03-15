#from importlib.resources import path
import os

def main():
    dir = input('Input file path : ')
    i = 1
    #path = 'C:/Users/BREEZE/Music/IMAGES/'
    path = dir
    for filename in os.listdir(path):
        my_dest = "img " + str(i) + ".jpg"
        source = path + filename
        dest = path + my_dest
        os.rename(source, dest)
        i += 1

if __name__ == '__main__':
    main()