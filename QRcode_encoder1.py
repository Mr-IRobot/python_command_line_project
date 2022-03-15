#from ensurepip import version
import qrcode


data = 'my python code'

img = qrcode.make(data)

img.save('C:/Users/BREEZE/Music/IMAGES/code/QRcode1.png')
