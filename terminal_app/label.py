# Class for labels

from PIL import Image, ImageDraw, ImageFont
import qrcode
from random import randint

class Label:

    def __init__(self, config: object):
        self.config = config

    def create(self, empid: str) -> list:
        """
        Create label file as PNG. Parameter data is dictionary with empid and labelid. 
        Return list with 2 elements: 
        list[0] is result code (0 - error, 1 - success), 
        list[1] is empty string or error message
        """
        try:
            # Get data for QR and label text
            data = self.generateData(empid)
            qr_data = f"{data['empid']}{data['labelid']}" # empid in XXXX format
            label_text = f"{empid}-{data['labelid']}"

            # Create QR
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=self.config.qr_box_size, border=self.config.qr_border)
            qr.add_data(qr_data)
            qr.make(fit=self.config.qr_fit)
            qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

            # Canvas
            label_size = self.config.label_size
            img = Image.new("RGB", label_size, "white")
            draw = ImageDraw.Draw(img)

            # Calculate sizes
            padding = self.config.padding
            gap = self.config.gap
            text_height = self.config.text_height

            # QR code takes remaining space
            available_height = label_size[1] - (2 * padding) - text_height - gap
            qr_size = min(available_height, label_size[0] - (2 * padding))  # keep it square

            # Paste QR centered horizontally, near top with padding
            qr_small = qr_img.resize((qr_size, qr_size))
            x_qr = (label_size[0] - qr_size) // 2
            y_qr = padding
            img.paste(qr_small, (x_qr, y_qr))

            # Draw text at bottom
            try:
                font = ImageFont.truetype(self.config.label_font_path, self.config.label_font_size)
            except Exception:
                font = ImageFont.load_default()

            bbox = draw.textbbox((0, 0), label_text, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]

            # Position text at bottom with padding
            y_text = label_size[1] - padding - h
            draw.text(((label_size[0] - w)//2, y_text), label_text, fill="black", font=font)

            # Save
            img.save(self.config.label_file)

            return [1, "Label image created"]
        except Exception as e:
            return [0, e]
            
    @staticmethod    
    def generateData(empid: str) -> dict:
        """
        Generate data for label. Return dict with empid in XXXX format and labelid.
        """
        # add trealing zeros to empid
        while len(empid) < 4:
            empid = "0" + empid

        # generate labelid using random number
        labelid = str(randint(1000000, 9999999))
        
        return {"empid": empid, "labelid": labelid}
