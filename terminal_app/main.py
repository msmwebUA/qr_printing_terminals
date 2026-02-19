from scan_card import ScanCard
from print_label import PrintLabel
from label import Label
from database import Database
# application config
from config import Config
# init configuration 
config = Config()

def main() -> None:
  # init database
  db = Database(config)
  # scan card
  print("Scan your card...")
  scan_obj = ScanCard(config)
  # read method returns list with 2 elements [code 0 or 1, error message or card data]
  scan_feedback = scan_obj.read()
  if scan_feedback[0] == 1:
    emp_id = scan_feedback[1]
    print("Scan was successful")
    # create label and print objects
    label_obj = Label(config)
    print_obj = PrintLabel(config)
    # number of copies as argument to print method
    copies = print_obj.getCopies()
    # print label
    print_feedback = print_obj.print(label_obj, emp_id, copies)
    if print_feedback[0] == 1:
      # add all printed label_ids to database
      printed_data = print_feedback[1]
      rows = []
      for label_id in printed_data["label_ids"]:
        row = int(f"{printed_data['emp_id']}{label_id}")
        rows.append((row,))
      db.addLabelId(rows)
      db_msg = ""
      print("Label was sent to printer")
    else:
      db_msg = print_feedback[1]
      # print printer error message
      print(print_feedback[1])
    # add log entry to db
    db.addLogEntry(emp_id, copies, db_msg)
  else:
    # add log entry to db
    db.addLogEntry(0, 0, scan_data[1])
    # print scan error message
    print(scan_data[1])

if __name__ == "__main__":
  main()