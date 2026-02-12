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
    label_feedback = label_obj.create(scan_feedback[1])
    if label_feedback[0] == 1:
      print("Label was created")
      # print label
      print_obj = PrintLabel(config)
      # number of copies as argument to print method
      copies = print_obj.getCopies()
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

if __name__ == "__main__":
  main()