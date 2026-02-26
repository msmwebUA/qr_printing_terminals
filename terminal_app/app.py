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
from PySide6.QtCore import Qt, QElapsedTimer, QTimer, QDateTime
from ui import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.setupUi(self)
    
    # init configuration 
    self.config = Config()

    # full screen UI
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    self.showFullScreen()
    # hide cursor
    self.setCursor(Qt.CursorShape.BlankCursor)
    # vars for exit from full screen mode
    self.click_count = 0
    self.click_timer = QElapsedTimer()

    # clock
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.updateClock)
    self.timer.start(1000)

    # set first stackedWidget page
    self.stackedWidget.setCurrentIndex(0)

    # connect slots (methods) to buttons on signals (events)
    self.startBtn.clicked.connect(self.scan)
    self.printBtn.clicked.connect(self.print)
    self.cancelBtnScan.clicked.connect(self.cancel)
    self.cancelBtnPrint.clicked.connect(self.cancel)

    # make cancel button on scan page unvisible (use timers for scan instead)
    self.cancelBtnScan.setVisible(False)

    # update copies value
    self.copiesSlider.valueChanged.connect(
      lambda value: self.copiesValue.setText(f"📑 Copies: {value} (move slider to change)")
    )
    # Info label about limits of copies
    self.copiesInfo.setText(f"ℹ️  Max {self.config.printer_max_copies_time} labels per time and {self.config.printer_max_copies_day} per day")

    # init database
    self.db = Database(self.config)
  
  def mousePressEvent(self, event) -> None:
    # Count clicks (reset, if > 2 sec)
    if self.click_count == 0 or self.click_timer.elapsed() > self.config.click_timeout:
        self.click_count = 1
        self.click_timer.start()
    else:
        self.click_count += 1
    # Check number of clicks
    if self.click_count >= self.config.click_to_exit:
        self.minimizeToWindow()
        self.click_count = 0 # reset counter
    # Allow the parent class to handle the event
    super().mousePressEvent(event)

  def minimizeToWindow(self) -> None:
    # Show frame and controls
    self.setWindowFlags(Qt.WindowType.Window)
    # Show cursor
    self.unsetCursor() 
    # Show in normal size
    self.showNormal() 
    self.activateWindow()

  def updateClock(self) -> None:
    now = QDateTime.currentDateTime()
    time_text = now.toString("HH:mm:ss")
    date_text = now.toString("dd.MM.yyyy")
    self.dateTimeLabel.setText(f"🗓️ {date_text}  ⏰ {time_text}")
  
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
      # set max copies
      copies_left = self.db.getCopiesLeft(self.emp_id)
      if copies_left > self.config.printer_max_copies_time:
        self.copiesSlider.setMaximum(self.config.printer_max_copies_time)
      elif copies_left > 0:
        self.copiesSlider.setMaximum(copies_left)
      else:
        # show alert and go back to start
        self.showAlert("Validation", "Sorry, but no more copies left today", "critical")
        return None # prevent further execution
      # set text to labels
      self.empName.setText("👷‍♂️ Employee: Unknown") 
      self.empId.setText(f"🆔 EmpID: {self.emp_id}")
      self.copiesLeft.setText(f"🏷️ Copies left: {copies_left}")
      self.copiesValue.setText(f"📑 Copies: {self.copiesSlider.value()} (move slider to change)")
      # move to next page
      self.stackedWidget.setCurrentIndex(2)
    else:
      err = str(scan_feedback[1])
      # add log entry to db
      self.db.addLogEntry(0, 0, err)
      # show error dialog
      self.showAlert("Scan Error", err, "critical")

  def print(self) -> None:
    # make Print button disabled
    self.printBtn.setEnabled(False)
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

  def cancel(self) -> None:
    # go back to start page
    self.stackedWidget.setCurrentIndex(0)
    # clear data
    self.clearData()

  def showAlert(self, title: str, text: str, alert_type: str) -> None:
    alert = QMessageBox(self)
    alert.setWindowTitle(title)
    alert.setText(text)
    if alert_type == "info":
        alert.setIcon(QMessageBox.Icon.Information)
    elif alert_type == "warning":
        alert.setIcon(QMessageBox.Icon.Warning)
    elif alert_type == "critical":
        alert.setIcon(QMessageBox.Icon.Critical)
    else:
        alert.setIcon(QMessageBox.Icon.Information)
    alert.setStandardButtons(QMessageBox.StandardButton.Ok)
    # Auto close
    QTimer.singleShot(self.config.alert_timeout, alert.accept)
    alert.exec()
    # After dialog closes
    self.stackedWidget.setCurrentIndex(0)
    self.clearData()

  def clearData(self) -> None:
    self.emp_id = None
    self.copiesSlider.setValue(1)
    self.empName.setText("Unknown employee")
    self.empId.setText("EmpID is not set")
    self.copiesLeft.setText("Copies left: ?")
    self.printBtn.setEnabled(True)
    gc.collect()
