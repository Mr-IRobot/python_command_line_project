from importlib.util import decode_source
from unittest import result
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/BREEZE/Music/IMAGES/code/download.png')

result = decode(img)

print (result)