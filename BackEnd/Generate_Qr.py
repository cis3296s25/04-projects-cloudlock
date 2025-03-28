import qrcode
from PIL import ImageTk

class QrImage(ImageTk.PhotoImage):
    """Generates an ImageTk.PhotoImage that contains the qrcode 
    Do not forget to save the image to global_image_list"""
    def __init__(self, text):
        self.qr = qrcode.QRCode()
        self.qr.add_data(text)
        self.qr.make()
        self.img = self.qr.make_image()
        super().__init__(image=self.img)