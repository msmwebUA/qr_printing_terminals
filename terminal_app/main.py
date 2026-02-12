from scan_card import ScanCard
from print_label import PrintLabel
from label import Label
# application config
from config import Config
# init configuration
config = Config()

def main() -> None:
  # scan card
  print("Scan your card...")
  scan_obj = ScanCard(config)
  # read method returns list with 2 elements [code 0 or 1, error message or card data]
  scan_feedback = scan_obj.read()
  if scan_feedback[0] == 1:
    print("Scan was successful")
    # create label
    label_obj = Label(config)
    label_feedback = label_obj.create({"empid": scan_feedback[1], "text": "Test"})
    if label_feedback[0] == 1:
      print("Label was created")
      # print label
      print_obj = PrintLabel(config)
      # number of copies as argument to print method
      copies = getCopies()
      print_feedback = print_label.print(copies)
      if print_feedback[0] == 1:
        print("Label was sent to printer")
      else:
        # print printer error message
        print(print_feedback[1])
    else:
      # print label error message
      print(label_data[1])
  else:
    # print scan error message
    print(scan_data[1])

def getCopies() -> int:
  """
  Asks user for number of copies, validates that input is an integer and returns the value.
  """
  while True:
    try:
      copies = int(input("Enter number of copies: ").strip())
      return copies
    except ValueError:
      print("Your input is not an integer! Try again...")

if __name__ == "__main__":
  main()