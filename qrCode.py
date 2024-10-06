import qrcode
qq = qrcode.QRCode()
info = input("enter data:")
qq.add_data(info)
qq.make()
img = qq.make_image()
img.save("a.png")