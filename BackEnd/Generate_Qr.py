import qrcode
from PIL import ImageTk, Image

class QrImage(ImageTk.PhotoImage):
    """Generates an ImageTk.PhotoImage that contains the qrcode 
    Do not forget to save the image to global_image_list"""
    def __init__(self, text, frame):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make()
        img = qr.make_image()

        frame.update()
        width = frame.winfo_width()
        height = frame.winfo_height()
        img.thumbnail((width, height), Image.Resampling.LANCZOS)
        super().__init__(image=img)