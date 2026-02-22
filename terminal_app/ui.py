# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 641, 421))
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.startFrame = QFrame(self.startPage)
        self.startFrame.setObjectName(u"startFrame")
        self.startFrame.setGeometry(QRect(0, 20, 641, 411))
        self.startFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.startFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.startFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dateTimeLabel = QLabel(self.startFrame)
        self.dateTimeLabel.setObjectName(u"dateTimeLabel")
        self.dateTimeLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_13.addWidget(self.dateTimeLabel, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.startBtn = QPushButton(self.startFrame)
        self.startBtn.setObjectName(u"startBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setMinimumSize(QSize(380, 190))
        self.startBtn.setStyleSheet(u"QPushButton {\n"
"    border-image: url(:/static/img/start.png) 0 0 0 0 stretch stretch;\n"
"    border: none; /* Removes the default button border */\n"
"}")
        self.startBtn.setCheckable(False)
        self.startBtn.setFlat(False)

        self.verticalLayout_13.addWidget(self.startBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.startPage)
        self.scanPage = QWidget()
        self.scanPage.setObjectName(u"scanPage")
        self.scanFrame = QFrame(self.scanPage)
        self.scanFrame.setObjectName(u"scanFrame")
        self.scanFrame.setGeometry(QRect(3, 15, 631, 411))
        self.scanFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.scanFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.scanFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.scanLabel = QLabel(self.scanFrame)
        self.scanLabel.setObjectName(u"scanLabel")
        font = QFont()
        font.setPointSize(40)
        self.scanLabel.setFont(font)
        self.scanLabel.setScaledContents(False)

        self.verticalLayout_14.addWidget(self.scanLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.scanImg = QLabel(self.scanFrame)
        self.scanImg.setObjectName(u"scanImg")
        self.scanImg.setPixmap(QPixmap(u":/static/img/scan.png"))
        self.scanImg.setScaledContents(True)

        self.verticalLayout_14.addWidget(self.scanImg, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.cancelBtnScan = QPushButton(self.scanFrame)
        self.cancelBtnScan.setObjectName(u"cancelBtnScan")
        self.cancelBtnScan.setMinimumSize(QSize(0, 50))
        self.cancelBtnScan.setMaximumSize(QSize(150, 16777215))

        self.verticalLayout_14.addWidget(self.cancelBtnScan, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.scanPage)
        self.printPage = QWidget()
        self.printPage.setObjectName(u"printPage")
        self.printFrame = QFrame(self.printPage)
        self.printFrame.setObjectName(u"printFrame")
        self.printFrame.setEnabled(True)
        self.printFrame.setGeometry(QRect(6, 13, 631, 411))
        self.printFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.printFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.printFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_1 = QFrame(self.printFrame)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.printImg = QLabel(self.frame_1)
        self.printImg.setObjectName(u"printImg")
        self.printImg.setFrameShape(QFrame.Shape.NoFrame)
        self.printImg.setPixmap(QPixmap(u":/static/img/printer.png"))

        self.horizontalLayout_7.addWidget(self.printImg, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(self.frame_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_2.setLineWidth(2)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_1 = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_1)

        self.empName = QLabel(self.frame_2)
        self.empName.setObjectName(u"empName")

        self.verticalLayout_11.addWidget(self.empName, 0, Qt.AlignmentFlag.AlignLeft)

        self.empId = QLabel(self.frame_2)
        self.empId.setObjectName(u"empId")

        self.verticalLayout_11.addWidget(self.empId, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalSpacer_2 = QSpacerItem(20, 26, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame_1)

        self.frame_3 = QFrame(self.printFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3.setLineWidth(3)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.copiesValue = QLabel(self.frame_3)
        self.copiesValue.setObjectName(u"copiesValue")

        self.verticalLayout_12.addWidget(self.copiesValue, 0, Qt.AlignmentFlag.AlignHCenter)

        self.copiesSlider = QSlider(self.frame_3)
        self.copiesSlider.setObjectName(u"copiesSlider")
        self.copiesSlider.setSingleStep(5)
        self.copiesSlider.setValue(0)
        self.copiesSlider.setOrientation(Qt.Orientation.Horizontal)
        self.copiesSlider.setInvertedControls(False)
        self.copiesSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.copiesSlider.setTickInterval(5)

        self.verticalLayout_12.addWidget(self.copiesSlider)

        self.copiesInfo = QLabel(self.frame_3)
        self.copiesInfo.setObjectName(u"copiesInfo")

        self.verticalLayout_12.addWidget(self.copiesInfo, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.printFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cancelBtnPrint = QPushButton(self.frame_4)
        self.cancelBtnPrint.setObjectName(u"cancelBtnPrint")
        self.cancelBtnPrint.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_8.addWidget(self.cancelBtnPrint)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.printBtn = QPushButton(self.frame_4)
        self.printBtn.setObjectName(u"printBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.printBtn.sizePolicy().hasHeightForWidth())
        self.printBtn.setSizePolicy(sizePolicy1)
        self.printBtn.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_8.addWidget(self.printBtn)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.printPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dateTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Date and Time", None))
        self.startBtn.setText("")
        self.scanLabel.setText(QCoreApplication.translate("MainWindow", u"Scan your card...", None))
        self.scanImg.setText("")
        self.cancelBtnScan.setText(QCoreApplication.translate("MainWindow", u"\u274c Cancel", None))
        self.printImg.setText("")
        self.empName.setText(QCoreApplication.translate("MainWindow", u"empName", None))
        self.empId.setText(QCoreApplication.translate("MainWindow", u"empId", None))
        self.copiesValue.setText(QCoreApplication.translate("MainWindow", u"copiesValue", None))
        self.copiesInfo.setText(QCoreApplication.translate("MainWindow", u"copiesInfo", None))
        self.cancelBtnPrint.setText(QCoreApplication.translate("MainWindow", u"\u274c Cancel", None))
        self.printBtn.setText(QCoreApplication.translate("MainWindow", u"\U0001f5a8\U0000fe0f PRINT", None))
    # retranslateUi

