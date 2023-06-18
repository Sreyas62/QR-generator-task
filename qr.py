import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.make(data)
    qr.save(filename)

print("Enter the Url for generating QR code : ")
data = input()
filename = "qr_code.png"
generate_qr_code(data, filename)
