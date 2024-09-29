import pyqrcode

url = input("Give the URL for make a QR : ")

qr_code = pyqrcode.create(url)

qr_code.svg("Qrcode.svg" , scale = 5)
