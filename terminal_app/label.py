# Class for labels

from PIL import Image, ImageDraw, ImageFont
import qrcode
from random import randint

class Label:

    def __init__(self, config: object, db: object) -> None:
        self.config = config
        self._db = db

    def create(self, emp_id: str, copies: int) -> list:
        """
        Create a label image with a QR code and text at the bottom.
        
        Parameters:
        emp_id (str): employee id
        copies (int): number of copies to generate
        
        Returns:
        list: list with 2 elements, 
        list[0] is result code (0 - error, 1 - success), 
        list[1] is error message or generated labels data for database processing
        """
        try:
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
                    qr_img = qr.make_image(fill_color="black", back_color="white").convert("1")

                    # Canvas
                    label_size = self.config.label_size
                    img = Image.new("1", label_size, 1) # 1 = white
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

                    # Position text
                    x_text = label_size[0] // 2
                    y_text = label_size[1] - padding
                    draw.text((x_text, y_text), label_text, fill=0, font=font, anchor="ms")

                    # Append label image
                    data["label_images"].append(img)
                    
                return [1, data]
            else:
                return [0, "No data for label"]
        except Exception as e:
            return [0, e]
               
    def generateData(self, emp_id: str, copies: int) -> dict:
        # add trealing zeros to emp_id
        """
        Generates data for labels.

        Parameters:
        emp_id (str): employee id
        copies (int): number of copies
        
        Returns:
        dict: dictionary with emp_id, copies, label_ids and label_images
        """
        while len(emp_id) < 4:
            emp_id = "0" + emp_id
        # init data
        data = {
                "emp_id": emp_id, # str in XXXX format
                "copies": copies,
                "label_ids": [],
                "label_images": []
            }
        # generate data with database check
        if self.config.label_id_check:
            return self._db.generateLabelData(data)
        # without database check
        else:
            for i in range(copies):
                data["label_ids"].append(str(randint(self.config.label_id_min, self.config.label_id_max)))
            
            return data
