import qrcode
from PIL import ImageTk

class QrImage(ImageTk.PhotoImage):
    """Generates an ImageTk.PhotoImage that contains the qrcode 
    Do not forget to save the image to global_image_list"""
    def __init__(self, text):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make()
        img = qr.make_image()
        super().__init__(image=img)