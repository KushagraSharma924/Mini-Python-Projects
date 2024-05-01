#import libraries such pyqrcode and png
import qrcode
import png
#Set dimensions for QrCode
qr_code = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr_code.add_data("https://www.google.com/")
qr_code.make(fit=True)
#Set color for QrCode
img = qr_code.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("QR Code Generated Successfully")