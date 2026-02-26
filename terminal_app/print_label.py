# Class for printing labels

from brother_ql.raster import BrotherQLRaster
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send

class PrintLabel:
  def __init__(self, config: object):
    self.config = config

  def print(self, label_obj: object, emp_id: str, copies: int,) -> list:
    """
    Convert label file and send to printer. Parameter copies is number of copies.
    Return list with 2 elements: 
    list[0] is result code (0 - error, 1 - success), 
    list[1] is empty string or error message
    """
    try:

      # TODO: check if printer is online
      # TODO: check if printer has paper

      # create labels
      label_feedback = label_obj.create(emp_id, copies)
      if label_feedback[0] == 1:
        # convert and send data to printer
        qlr = BrotherQLRaster(self.config.printer_model)
        instructions = convert(
            qlr = qlr,
            images = label_feedback[1]["label_files"],
            label = self.config.label_type,
            rotate = '0',
            cut = False,
            left_margin = 0
          )
        status = send(instructions, self.config.printer_address)
        # return "success" and generated labels data for database processing
        if status["did_print"]:
          return [1, label_feedback[1]]
        else:
          raise RuntimeError("Response from printer: Failed to print label")
      else:
        # return error message received from label object
        return [0, "Failed to create label: " + label_feedback[1]]
    # return error
    except Exception as e:
      return [0, e]

  def getCopies(self) -> int:
    """
    Asks user for number of copies, validates that input is an integer and returns the value.
    """
    max_copies = self.config.printer_max_copies
    while True:
      try:
        copies = int(input("Enter number of copies: ").strip())
        if 1 <= copies <= max_copies:
          return copies
        else:
          print(f"Min 1 and max {max_copies} copies allowed. Try again...")
      except ValueError:
        print("Your input is not an integer! Try again...")
