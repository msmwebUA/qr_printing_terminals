# Class for labels

from PIL import Image, ImageDraw, ImageFont
import qrcode
from random import randint
from pathlib import Path

class Label:

    def __init__(self, config: object, db: object):
        self.config = config
        self._db = db

    def create(self, emp_id: str, copies: int) -> list:
        """
        Create label file as PNG. Parameter data is dictionary with emp_id and label_id. 
        Return list with 2 elements: 
        list[0] is result code (0 - error, 1 - success), 
        list[1] is dict of label data or error message
        """
        try:
            # Clear directory with label files
            for file in Path(self.config.label_path).iterdir():
                if file.is_file():
                    file.unlink()

            # Get data for QR and label text
            data = self.generateData(emp_id, copies)
            if data:
                emp_id_xxxx = data["emp_id"]
                for i in range(copies):
                    label_id = data['label_ids'][i]
                    qr_data = f"{emp_id_xxxx}{label_id}" # emp_id in XXXX format
                    label_text = f"{emp_id}-{label_id}" # emp_id as is

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
                    padding = self.config.label_padding
                    gap = self.config.label_gap
                    text_height = self.config.label_text_height

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
                    fname = f"{self.config.label_file}-{i}{self.config.label_file_extension}"
                    img.save(fname)
                    data["label_files"].append(fname)
                    
                return [1, data]
            else:
                return [0, "No data for label"]
        except Exception as e:
            return [0, e]
               
    def generateData(self, emp_id: str, copies: int) -> dict:
        """
        Generate data for labels. Return dict with emp_id as str in XXXX format and label_ids as list.
        """
        # add trealing zeros to emp_id
        while len(emp_id) < 4:
            emp_id = "0" + emp_id
        # init data
        data = {
                "emp_id": emp_id, # str in XXXX format
                "copies": copies,
                "label_ids": [],
                "label_files": []
            }
        # generate data with database check
        if self.config.label_id_check:
            return self._db.generateLabelData(data)
        # without database check
        else:
            for i in range(copies):
                data["label_ids"].append(str(randint(self.config.label_id_min, self.config.label_id_max)))
            
            return data
