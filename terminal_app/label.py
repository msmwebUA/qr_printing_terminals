# Class for labels

from PIL import Image, ImageDraw, ImageFont
import qrcode

class Label:

    def __init__(self, config: object):
        self.config = config

    def create(self, data: dict) -> list:
        """Create label file as PNG. Parameter data is dictionary with empid and text. 
        Return list with 2 elements: 
            list[0] is result code (0 - error, 1 - success), 
            list[1] is empty string or error message"""
        try:
            # Create QR
            empid = data["empid"]
            text = data["text"]
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=self.config.qr_box_size, border=self.config.qr_border)
            qr.add_data(empid)
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

            bbox = draw.textbbox((0, 0), text, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]

            # Position text at bottom with padding
            y_text = label_size[1] - padding - h
            draw.text(((label_size[0] - w)//2, y_text), text, fill="black", font=font)

            # Save
            img.save(self.config.label_file)
            return [1, "Label image created"]
        except Exception as e:
            return [0, e]