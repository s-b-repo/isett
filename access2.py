import qrcode

def generate_qrcode(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("iphone_qrcode.png")

def give_root_access():
    data = "root_access:true"
    generate_qrcode(data)

def enable_developer_mode():
    data = "developer_mode:true"
    generate_qrcode(data)

def enable_sideloading():
    data = "sideloading:true"
    generate_qrcode(data)

give_root_access()
enable_developer_mode()
enable_sideloading()
