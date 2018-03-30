from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#from mqtt.MQTTgui import MQTTlayer
#from rstp.RSTPgui import RSTPlayer
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(100, 100, 240, 50))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.setText("(1)Pre-preparation for New Mission")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 150, 200, 150))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttonsarea = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttonsarea.setContentsMargins(0, 0, 0, 0)
        self.buttonsarea.setObjectName("buttonsarea")
        self.pushButton_mqtt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_mqtt.setObjectName("pushButton_mqtt")
        self.buttonsarea.addWidget(self.pushButton_mqtt)
        self.pushButton_rstp = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_rstp.setObjectName("pushButton_rstp")
        self.buttonsarea.addWidget(self.pushButton_rstp)
        self.pushButton_events = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_events.setObjectName("pushButton_events")
        self.buttonsarea.addWidget(self.pushButton_events)
        self.pushButton_map = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_map.setObjectName("pushButton_map")
        self.buttonsarea.addWidget(self.pushButton_map)

        self.pushButton_start.clicked.connect(self.openpre)
        self.pushButton_mqtt.clicked.connect(self.openMQTT)
        self.pushButton_rstp.clicked.connect(self.openRSTP)
        self.pushButton_map.clicked.connect(self.openMAP)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 250, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 87, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_ = QtWidgets.QLabel(self.centralwidget)
        self.label_.setGeometry(QtCore.QRect(100, 40, 290, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_.setFont(font)
        self.label_.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_.setObjectName("label_")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(90, 400, 261, 91))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("obee-logo.png"))
        self.label_logo.setObjectName("label_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OBEE Quick Access Screen"))
        self.pushButton_mqtt.setText(_translate("MainWindow", "open MQTT set"))
        self.pushButton_rstp.setText(_translate("MainWindow", "open RSTP set"))
        self.pushButton_map.setText(_translate("MainWindow", "Mission Map"))
        self.pushButton_events.setText(_translate("MainWindow", "(2)Store Events"))
        self.label.setText(_translate("MainWindow", "Check your connection settings>>>"))
        self.label_.setText(_translate("MainWindow", ">>> before starting the new mission"))

    def openpre(self):
        import sqlite3
        # SQLite DB Name
        DB_Name =  "dbMQTT.db"

        # SQLite DB Table Schema
        TableSchema="""
        drop table if exists Weather_Data ;
        create table weather (
          _id_ integer primary key autoincrement,
          ID text,
          Date_n_Time text,
          weather_value text
        );


        drop table if exists Sensor_Data ;
        create table sensor (
          _id_ integer primary key autoincrement,
          ID text,
          Date_n_Time text,
          Sensor_value text
        );


        drop table if exists Location_Data ;
        create table location (
          loc text
        );
        """

        #Connect or Create DB File
        conn = sqlite3.connect(DB_Name)
        curs = conn.cursor()

        #Create Tables
        sqlite3.complete_statement(TableSchema)
        curs.executescript(TableSchema)

        #Close DB
        curs.close()
        conn.close()

        QMessageBox.about(self.centralwidget, str("Successful"), str("Database created"))

    def premaps(self):
        import sqlite3
        import json
        import codecs

        conn = sqlite3.connect('dbMQTT.db')
        cur = conn.cursor()

        fhand = codecs.open('where.js','w', "utf-8")
        fhand.write("myData = [\n")
        count = 0

        cur.execute('SELECT * FROM location')
        for row in cur :

            loc = str(row[0])#0. sutunu okuduk
            if loc == 0 : continue
            try :
                print(loc)

                count = count + 1
                if count > 1 : fhand.write(",\n")
                output = "["+str(loc)+"]"
                fhand.write(output)
            except:
                continue

        fhand.write("\n];\n")
        cur.close()
        fhand.close()

    def openMQTT(self):#yeni komut istemi

        if sys.platform == "linux": # for Linux
            os.system("gnome-terminal -e 'python3 MQTTgui.py'")
        elif sys.platform == "win32": # for Windows
            os.system("start cmd /c 'python3 MQTTgui.py'")

    def openRSTP(self):
        if sys.platform == "linux": # for Linux
            os.system("gnome-terminal -e 'python3 RSTPgui.py'")
        elif sys.platform == "win32": # for Windows
            os.system("start cmd /c 'python3 RSTPgui.py'")

    def openMAP(self):
        import webbrowser
        self.premaps()
        webbrowser.open('where.html')

    #def openEVENTS(self):

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
