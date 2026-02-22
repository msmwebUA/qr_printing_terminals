# from scan_card import ScanCard
# from print_label import PrintLabel
# from label import Label
# from database import Database
# # application config
# from config import Config
# # init configuration 
# config = Config()

# import UI
from PySide6.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    # set first stackedWidget page
    self.stackedWidget.setCurrentIndex(0)

    # connect slots (methods) to buttons on signals (events)
    self.startBtn.clicked.connect(self.start)
    self.printBtn.clicked.connect(self.print)
    self.cancelBtnScan.clicked.connect(self.cancel)
    self.cancelBtnPrint.clicked.connect(self.cancel)

  
  def start(self):
    self.stackedWidget.setCurrentIndex(1)
    # TODO: start scan
    # TODO: move to print page when scan is successful

  def print(self):
    pass

  # return to start page
  def cancel(self):
    # go back to start page
    self.stackedWidget.setCurrentIndex(0)
    # TODO: clear data

# def main() -> None:
#   # init database
#   db = Database(config)
#   # scan card
#   print("Scan your card...")
#   scan_obj = ScanCard(config)
#   # read method returns list with 2 elements [code 0 or 1, error message or card data]
#   scan_feedback = scan_obj.read()
#   if scan_feedback[0] == 1:
#     emp_id = scan_feedback[1]
#     print("Scan was successful")
#     # create label and print objects
#     label_obj = Label(config)
#     print_obj = PrintLabel(config)
#     # number of copies from user input
#     copies = print_obj.getCopies()
#     # create and print labels
#     print_feedback = print_obj.print(label_obj, emp_id, copies)
#     if print_feedback[0] == 1:
#       # add all printed label_ids to database
#       printed_data = print_feedback[1]
#       rows = []
#       for label_id in printed_data["label_ids"]:
#         row = int(f"{printed_data['emp_id']}{label_id}")
#         rows.append((row,))
#       db.addLabelId(rows)
#       db_msg = None
#       print("Label was sent to printer")
#     else:
#       db_msg = str(print_feedback[1])
#       # print printer error message
#       print(print_feedback[1])
#       # inform user about common errors in clear way
#       if 'Errno 110' or 'Failed to print' in db_msg:
#         print("Something wrong with printer. Are there labels in roll or is cover closed?")
#       if 'Device not found' in db_msg:
#         print("Check connection to printer")
#     # add log entry to db
#     db.addLogEntry(emp_id, str(copies), db_msg)
#   else:
#     # add log entry to db
#     db.addLogEntry(0, 0, str(scan_data[1]))
#     # print scan error message
#     print(scan_data[1])