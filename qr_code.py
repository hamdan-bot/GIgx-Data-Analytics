import qrcode 
from qrcode.image.pure import PyPNGImage
data= input("Enter the data to be encoded in the QR code or url: ").strip()
filename = input("enter the filename to save the QR code: ").strip()
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")