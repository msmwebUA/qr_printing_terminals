# Prepare the printer_identifier
# brother_ql commonly accepts a URI like:
# usb://0x<VENDOR>:0x<PRODUCT>
# You can also try /dev/usb/lp0 or CUPS if you installed/used CUPS instead — 
# but usb:// is the usual direct method for brother_ql.


from PIL import Image, ImageDraw, ImageFont
import qrcode
from brother_ql.raster import BrotherQLRaster
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send

# --- settings ---
MODEL = "QL-700"                  # change to your model (QL-700, QL-800, etc.)
PRINTER = "usb://0x04f9:0x2042"   # replace with your vendor:product from lsusb
LABEL_TYPE = "23x23"              # 23mm square labels (the brother_ql label name)
OUTFILE = "label_23x23.png"

# --- create QR ---
data = "9990101010101"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=3, border=1)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# --- canvas: Brother printable area for 23mm roll is 202x202 px ---
label_size = (202, 202)
img = Image.new("RGB", label_size, "white")
draw = ImageDraw.Draw(img)

# --- calculate sizes with padding ---
padding = 5  # 5-10px as you mentioned
text_height = 20  # reserve space for text at bottom
gap = 5  # small gap between QR and text

# QR code takes remaining space
available_height = label_size[1] - (2 * padding) - text_height - gap
qr_size = min(available_height, label_size[0] - (2 * padding))  # keep it square

# paste QR centered horizontally, near top with padding
qr_small = qr_img.resize((qr_size, qr_size))
x_qr = (label_size[0] - qr_size) // 2
y_qr = padding
img.paste(qr_small, (x_qr, y_qr))

# draw text at bottom
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
except Exception:
    font = ImageFont.load_default()

text = "ID 999"
bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]

# position text at bottom with padding
y_text = label_size[1] - padding - h
draw.text(((label_size[0] - w)//2, y_text), text, fill="black", font=font)

# paste QR centered top
# qr_size = 120
# qr_small = qr_img.resize((qr_size, qr_size))
# x_qr = (label_size[0] - qr_size) // 2
# img.paste(qr_small, (x_qr, 14))

# draw text under QR
# try:
#    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
# except Exception:
#    font = ImageFont.load_default()
#
# text = "ID 999"
# bbox = draw.textbbox((0, 0), text, font=font)
# w = bbox[2] - bbox[0]
# h = bbox[3] - bbox[1]
# draw.text(((label_size[0] - w)//2, qr_size + 24), text, fill="black", font=font)

img.save(OUTFILE)

# --- convert and print ---
qlr = BrotherQLRaster(MODEL)
instructions = convert(qlr=qlr, images=[OUTFILE], label=LABEL_TYPE, rotate='0')
send(instructions, PRINTER)
print("Printed test label.")