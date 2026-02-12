# Class for application configuration

from pathlib import Path

class Config():
  
  def __init__(self):
    # APPLICATION CONFIG

    # SCANNING
    # max scan times per read action
    self.max_scans = 30

    # PRINTER
      # brother_ql commonly accepts a URI like:
      # usb://0x<VENDOR>:0x<PRODUCT>
      # You can also try /dev/usb/lp0 or CUPS if you installed/used CUPS instead — 
      # but usb:// is the usual direct method for brother_ql.
    self.printer_model = "QL-700"
    self.printer_address = "usb://0x04f9:0x2042" # replace with your vendor:product from lsusb
    self.printer_max_copies = 50

    # QR CODE
    self.qr_box_size = 3
    self.qr_border = 1
    self.qr_fit = True

    # LABEL IMAGE
    self.label_type = "23x23" # 23mm square labels
    self.label_size = (202, 202) # Brother printable area for 23mm roll is 202x202 px
    self.label_padding = 5  # px
    self.label_text_height = 20  # reserve space for text at bottom
    self.label_gap = 5  # small gap between QR and text
    self.label_font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    self.label_font_size = 14
    self.label_id_min = 1000000
    self.label_id_max = 9999999
    self.label_file = "labels/label_23x23.png"
    # create labels dir if not exists
    main_dir = Path(__file__).parent
    labels_path = script_dir / "labels"
    labels_path.mkdir(exist_ok=True)