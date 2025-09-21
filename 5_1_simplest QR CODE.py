import pyqrcode,png,os

import matplotlib.pyplot as plt
import matplotlib.image as img

data=input("Please Enter text for which QR CODE TO BE GENRATED")
url=pyqrcode.create(data)
url.png('techdev.png',scale=7)
print('QR Code genrated at',os.getcwd())

image=img.imread("techdev.png")
plt.imshow(image)
plt.axis("off")
plt.title("By:Bhupendra Khairani")
plt.show()
