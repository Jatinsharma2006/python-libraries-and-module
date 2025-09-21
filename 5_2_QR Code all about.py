import pyqrcode
from pyqrcode import QRCode
import sys
#two was to create qr code 1 is using pyqrcode.create and 2 is using QRCode 

#1
url = pyqrcode.create('http://uca.edu')
url.svg('uca.svg', scale=10)
url.show(wait=2.4)

#2
number = QRCode(123456789012345)
number.png('big-number.png')
number.show(wait=2.4)

#SYNTAX
#pyqrcode.create(content, error='H','Q','M','L', version=None, mode=None, encoding=None)
"""
error correction level :- the higher error correction levels make the QR Code easier to
scan even when it is partially damaged also increase the size of QR CODE
L(low)recovers 7%of data,M(Medium)recovers 15%of data,Q(Quartile)recovers 25%of data,
H(HIGH)recovers 30%of data

we dont need to set all these pyqrcode library automatically sets them based on content
"""



#QR Code : Color change ,module color-foreground,background
" It accept value from 0 to 255 in RGB and fourth is for transparancy,quit_zone distance between qr and its border"
#SYNTAX
#png(file, scale=1, module_color=(0, 0, 0, 255), background=(255, 255, 255, 255), quiet_zone=4)

#EX_1
code = pyqrcode.create('Are you suggesting coconuts migrate?')
code.png('swallow.png', scale=5)
code.png('swallow.png', scale=5,
             module_color=(0x66, 0x33, 0x0),      #Dark brown
             background=(0xff, 0xff, 0xff, 0x88)) #50% transparent white
#EX_2
code = pyqrcode.create('Are you suggesting coconuts migrate?')
code.png('allow.png', scale=5)
code.png('allow.png', scale=5,
             module_color=(255, 150, 150),      
             background=(200, 170, 100, 255))

#SHOW FN
#show(wait=1.2, scale=10, module_color=(0, 0, 0, 255), background=(255, 255, 255, 255), quiet_zone=4)

#USE CASE : PNG FILE NAME .SHOW()
big_code = pyqrcode.create('0987654321', error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=(0, 0, 0, 128), background=(0xff, 0xff, 0xcc))
big_code.show()          #here 



#QR CODE result in terminal 
"terminal(module_color='default', background='reverse', quiet_zone=4)"
code = pyqrcode.create('Example')
text = code.terminal()
print(text)


#QR CODE result in terminal in Binary format
"text(quiet_zone=4)"
code = pyqrcode.create('Example')
text = code.text()
print(text)


