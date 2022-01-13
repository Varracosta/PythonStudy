import qrcode
import image

data = input("Enter any info you wish to encode in QRCode: ")
qr_image = qrcode.make(data)
qr_image.save('C:/Users/starw/Desktop/qrcode.png')