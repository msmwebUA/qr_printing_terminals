from scan_card import ScanCard
from print_label import PrintLabel
from label import Label
from database import Database
# application config
from config import Config
# garbage cleaning
import gc

# import UI
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication
from ui import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

    # set first stackedWidget page
    self.stackedWidget.setCurrentIndex(0)

    # connect slots (methods) to buttons on signals (events)
    self.startBtn.clicked.connect(self.scan)
    self.printBtn.clicked.connect(self.print)
    self.cancelBtnScan.clicked.connect(self.cancel)
    self.cancelBtnPrint.clicked.connect(self.cancel)

    # update copies value
    self.copiesSlider.valueChanged.connect(
      lambda value: self.copiesValue.setText(f"Copies: {value}")
    )

    # init configuration 
    self.config = Config()

    # init database
    self.db = Database(self.config)
  
  def scan(self) -> None:
    self.stackedWidget.setCurrentIndex(1)
    QApplication.processEvents() # refresh page immediately
    # scan card
    scan_obj = ScanCard(self.config)
    # read method returns list with 2 elements [code 0 or 1, error message or card data]
    scan_feedback = scan_obj.read()
    if scan_feedback[0]:
      # assign emp_id variable
      self.emp_id = scan_feedback[1]
      # set text to labels
      self.empId.setText(f"EmpID: {self.emp_id}")
      self.empName.setText("Employee: Unknown") 
      # set max copies
      copies_left = self.db.getCopiesLeft(self.emp_id)
      if copies_left > self.config.printer_max_copies_time:
        self.copiesSlider.setMaximum(self.config.printer_max_copies_time)
      elif copies_left > 0:
        self.copiesSlider.setMaximum(copies_left)
      else:
        self.showAlert("Validation", "No more copies left today", "critical")
      # move to next page
      self.stackedWidget.setCurrentIndex(2)
    else:
      err = str(scan_feedback[1])
      # show error dialog
      self.showAlert("Scan Error", err, "critical")
      # add log entry to db
      self.db.addLogEntry(0, 0, err)

  def print(self) -> None:
    # create label and print objects
    label_obj = Label(self.config, self.db)
    print_obj = PrintLabel(self.config)
    copies = self.copiesSlider.value()
    # create and print labels
    print_feedback = print_obj.print(label_obj, self.emp_id, copies)
    if print_feedback[0]:
      # add all printed label_ids to database
      printed_data = print_feedback[1]
      rows = []
      for label_id in printed_data["label_ids"]:
        row = int(f"{printed_data['emp_id']}{label_id}")
        rows.append((row,))
      self.db.addLabelId(rows)
      # add log entry to db
      self.db.addLogEntry(self.emp_id, str(copies), None)
      # show success dialog
      self.showAlert("Print label", "Label was sent to printer", "info")
    else:
      error = str(print_feedback[1])
      alert = None
      # inform user about common errors in clear way
      if 'Errno 110' in error or 'Failed to print' in error:
        alert = "Something wrong with printer. Are there labels in roll or is cover closed?"
      if 'Device not found' in error:
        alert = "Check connection to printer"
      # add log entry to db
      self.db.addLogEntry(self.emp_id, str(copies), error)
      # show alert and clear data
      self.showAlert("Print Error", alert if alert else error, "critical")

  # return to start page
  def cancel(self) -> None:
    # go back to start page
    self.stackedWidget.setCurrentIndex(0)
    # clear data
    self.clearData()

  def showAlert(self, title: str, text: str, alert_type: str) -> None:
    if alert_type == "info":
      QMessageBox.information(self,title, text)
    elif alert_type == "warning":
      QMessageBox.warning(self, title, text)
    elif alert_type == "critical":
      QMessageBox.critical(self, title, text)
    else:
      QMessageBox.information(self, title, text)
    # go back to start page (user clicked OK or X in modal dialog)
    self.stackedWidget.setCurrentIndex(0)
    # clear data
    self.clearData()

  def clearData(self):
    self.emp_id = None
    self.copiesSlider.setValue(1)
    self.empName.setText("Unknown employee")
    self.empId.setText("EmpID is not set")
    gc.collect()
