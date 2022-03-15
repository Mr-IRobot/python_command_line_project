from distutils.cmd import Command
import sys
import json
#import multi_clipboard
import clipboard

saved_data  = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1:]
    data = load_data(save_data)

    if command == "save":
        key = input("Input a key: ")
        data[key] = clipboard.paste()
        save_data(saved_data, data)
        print ("Data saved!")
    elif command == "load":
        key = input("Enter the key: ")
        if key in data:
            clipboard.copy(data[key])
            print ("Data copied to clipboard!")
        else:
            print ("Key doesn't exist, Pls enter a valid key")
    elif command == "list":
        print (data)
else:
    print ("You entered multiple commands, Pls choose only one ")