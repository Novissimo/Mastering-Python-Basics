from pyzbar.pyzbar import decode
from PIL import Image
picture = Image.open("roger.jpg")
qr = decode(picture)
text = qr[0].data.decode()
print('text: {}'.format(text))