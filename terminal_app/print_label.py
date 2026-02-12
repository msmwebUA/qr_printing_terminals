# Class for printing labels

from brother_ql.raster import BrotherQLRaster
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send

class PrintLabel:
  def __init__(self, config: object):
    self.config = config

  def print(self, copies: int) -> list:
    """Convert label file and send to printer. Parameter copies is number of copies.
    Return list with 2 elements: 
        list[0] is result code (0 - error, 1 - success), 
        list[1] is empty string or error message"""
    try:
      qlr = BrotherQLRaster(self.config.printer_model)
      images = [self.config.label_file] * copies  # same label image repeated
      instructions = convert(
        qlr = qlr,
        images = images,
        label = self.config.label_type,
        rotate = '0'
      )
      send(instructions, self.config.printer_address)
      return [1, "Label was sent to printer"]
    except Exception as e:
      return [0, e]