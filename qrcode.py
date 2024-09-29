import pyqrcode

url = input("QR kod yapmak için url verin : ")

qr_code = pyqrcode.create(url)

qr_code.svg("Qrcode.svg" , scale = 5)
