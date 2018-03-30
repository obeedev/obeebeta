import os
import sys
import VLC
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, QVBoxLayout, QAction, QFileDialog, QApplication

class obeeUi(QMainWindow):

    def __init__(self, master=None):
            QMainWindow.__init__(self, master)
            self.setWindowTitle("OBEE Control Center")

            # creating a basic vlc instance
            self.instance = VLC.Instance()
            # creating an empty vlc media player
            self.mediaplayer = self.instance.media_player_new()

            self.MainUi()
            ##self.MapLayer()
            self.temelmenubar()
            self.isPaused = False
            self.openQ()


    def MainUi(self):
        """
        Kullanıcı arayüz yapılandırması-sinyal/slot
        """
        #_translate = QtCore.QCoreApplication.translate
        self.Main_widget = QtWidgets.QWidget(self)
        self.palette = self.Main_widget.palette()
        self.palette.setColor (QPalette.Window,QColor(193,193,193))
        self.Main_widget.setPalette(self.palette)
        self.Main_widget.setAutoFillBackground(True)

        self.setObjectName("Main_widget")
        self.setCentralWidget(self.Main_widget)
        self.setWindowTitle("obee")

        #LOGO yu buraya koyduk
        self.label_logo = QtWidgets.QLabel(self.Main_widget)
        self.label_logo.setGeometry(QtCore.QRect(950, 600, 261, 91))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("obee-logo.png"))
        self.label_logo.setObjectName("label_logo")
        self.label_logo.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_logo.setMouseTracking(True)

        #1.KISIM-RSTPlayer
        self.videoframe = QFrame(self.Main_widget)
        self.videoframe.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.palette = self.videoframe.palette()
        self.palette.setColor (QPalette.Window,QColor(0,0,0))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)

        self.RSTPbutton = QPushButton(self.Main_widget)#1.BUTON
        self.RSTPbutton.setGeometry(QtCore.QRect(0, 600, 50, 50))
        self.RSTPbutton.setText("RSTP")
        self.palette = self.RSTPbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(0,0,0))
        self.RSTPbutton.setPalette(self.palette)
        self.RSTPbutton.setAutoFillBackground(True)
        self.RSTPbutton.clicked.connect(self.Stream)
        self.RSTbutton = QPushButton(self.Main_widget)#2.BUTON
        self.RSTbutton.setGeometry(QtCore.QRect(50, 600, 50, 50))
        self.RSTbutton.setText("X")
        self.palette = self.RSTbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(255,255,255))
        self.RSTbutton.setPalette(self.palette)
        self.RSTbutton.setAutoFillBackground(True)
        self.RSbutton = QPushButton(self.Main_widget)#3.BUTON
        self.RSbutton.setGeometry(QtCore.QRect(0, 650, 50, 50))
        self.RSbutton.setText("Y")
        self.palette = self.RSTPbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(255,255,255))
        self.RSbutton.setPalette(self.palette)
        self.RSbutton.setAutoFillBackground(True)
        self.Rbutton = QPushButton(self.Main_widget)#4.BUTON
        self.Rbutton.setGeometry(QtCore.QRect(50, 650, 50, 50))
        self.Rbutton.setText("Z")
        self.palette = self.RSTPbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(255,255,255))
        self.Rbutton.setPalette(self.palette)
        self.Rbutton.setAutoFillBackground(True)#---
        self.f1button = QtWidgets.QPushButton(self.Main_widget)#1.BUTON
        self.f1button.setGeometry(QtCore.QRect(800, 600, 50, 50))
        self.f1button.setText("F1")
        self.f2button = QtWidgets.QPushButton(self.Main_widget)#2.BUTON
        self.f2button.setGeometry(QtCore.QRect(850, 600, 50, 50))
        self.f2button.setText("F2")
        self.f3button = QPushButton(self.Main_widget)#3.BUTON
        self.f3button.setGeometry(QtCore.QRect(800, 650, 50, 50))
        self.f3button.setText("F3")
        self.f4button = QPushButton(self.Main_widget)#4.BUTON
        self.f4button.setGeometry(QtCore.QRect(850, 650, 50, 50))
        self.f4button.setText("F4")

        self.f1button.clicked.connect(self.openQ)
        self.f2button.clicked.connect(self.fopenpre)
        #self.f3button.clicked.connect(self.fopendbupdate)
        self.f4button.clicked.connect(self.fopenhelp)

        #---info function button label---
        self.label_f1 = QtWidgets.QLabel(self.Main_widget)
        self.label_f1.setGeometry(QtCore.QRect(600, 585, 200, 50))
        self.label_f1.setText("*(F1)Quick Access Screen")
        self.label_f2 = QtWidgets.QLabel(self.Main_widget)
        self.label_f2.setGeometry(QtCore.QRect(600, 605, 200, 50))
        self.label_f2.setText("*(F2)Pre-paration DB")
        self.label_f3 = QtWidgets.QLabel(self.Main_widget)
        self.label_f3.setGeometry(QtCore.QRect(600, 625, 200, 50))
        self.label_f3.setText("*(F3)Database Update")
        self.label_f4 = QtWidgets.QLabel(self.Main_widget)
        self.label_f4.setGeometry(QtCore.QRect(600, 645, 200, 50))
        self.label_f4.setText("*(F4)-Help?")

        #2.KISIM-Map
        self.mapFrame = QFrame(self.Main_widget)
        self.mapFrame.setGeometry(QtCore.QRect(900, 0, 350, 450))
        self.palette = self.mapFrame.palette()
        self.palette.setColor (QPalette.Window,QColor(0,220,0))
        self.mapFrame.setPalette(self.palette)
        self.mapFrame.setAutoFillBackground(True)
        self.mapFrame.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label = QtWidgets.QLabel(self.mapFrame)
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
        self.label.setText("BETA***")

        self.mapbutton = QPushButton(self.Main_widget)#1.BUTON
        self.mapbutton.setGeometry(QtCore.QRect(1250, 400, 50, 50))
        self.mapbutton.setText("MAP")
        self.mapbutton.setPalette(self.palette)
        self.mapbutton.clicked.connect(self.viewhtml)


        #3.KISIM-EVENTS
        self.eventFrame = QFrame(self.Main_widget)
        self.eventFrame.setGeometry(QtCore.QRect(900, 450, 350, 150))
        self.palette = self.mapFrame.palette()
        self.palette.setColor (QPalette.Window,QColor(220,0,0))
        self.eventFrame.setPalette(self.palette)
        self.eventFrame.setAutoFillBackground(True)

        self.events_textBrowser = QtWidgets.QTextBrowser(self.Main_widget)
        self.events_textBrowser.setGeometry(QtCore.QRect(910, 460, 330, 130))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 138, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 235, 231))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.events_textBrowser.setPalette(palette)


        self.eventbutton = QPushButton(self.Main_widget)#1.BUTON
        self.eventbutton.setGeometry(QtCore.QRect(1250, 450, 50, 50))
        self.eventbutton.setText("EVENT")
        self.eventbutton.setPalette(self.palette)
        self.eventbutton.clicked.connect(self.Event)


        self.resize(1300, 900)
        self.show()


    def openQ(self):#yeni komut istemi
        if sys.platform == "linux": # for Linux
            os.system("gnome-terminal -e 'python3 startquick_basic.py'")
        elif sys.platform == "win32": # for Windows
            os.system("start cmd /c 'python3 startquick_basic.py'")

    def fopenpre(self):
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

        QMessageBox.about(self.Main_widget, str("Complete"), str("Database created//but(for error) you should delete or replace old database file"))

    def fopenhelp(self):
        """import webbrowser
        self.pre..()
        webbrowser.open('help.html')"""

    def MQTTlayersetupUi(self):
        self.MQTTsetup = QtWidgets.QWidget(self)
        self.setCentralWidget(self.MQTTsetup)
        self.MQTTsetup.setObjectName("MQTTsetup")
        #Objeleri yerleştirelim
        ###1.KISIM###
        self.groupBox = QtWidgets.QGroupBox(self.MQTTsetup)
        self.palette = self.groupBox.palette()
        self.palette.setColor (QPalette.Window,QColor(143,143,143))
        self.groupBox.setPalette(self.palette)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 71))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.label_info = QtWidgets.QLabel(self.groupBox)
        self.label_info.setGeometry(QtCore.QRect(77, 50, 282, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.label_info.setFont(font)
        self.label_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_info.setObjectName("label_info")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(430, 10, 81, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Connect_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Connect_pushButton.setObjectName("Connect_pushButton")
        self.Connect_pushButton.clicked.connect(self.MQTTclient)
        self.verticalLayout.addWidget(self.Connect_pushButton)
        self.Disconnect_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Disconnect_pushButton.setObjectName("Disconnect_pushButton")
        #self.Disconnect_pushButton.clicked.connect(self.MQTTstop)
        self.verticalLayout.addWidget(self.Disconnect_pushButton)
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 20, 261, 22))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_host = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_host.setContentsMargins(0, 0, 0, 0)
        self.formLayout_host.setObjectName("formLayout_host")
        self.connectionsetup_host_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.connectionsetup_host_label.setObjectName("connectionsetup_host_label")
        self.formLayout_host.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.connectionsetup_host_label)
        self.Host_linedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Host_linedit.setObjectName("Host_linedit")
        self.formLayout_host.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Host_linedit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(270, 20, 141, 21))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_port = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_port.setContentsMargins(0, 0, 0, 0)
        self.formLayout_port.setObjectName("formLayout_port")
        self.Port_linedit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.Port_linedit.setObjectName("Port_linedit")
        self.formLayout_port.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Port_linedit)
        self.connectionsetup_port_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.connectionsetup_port_label.setObjectName("connectionsetup_port_label")
        self.formLayout_port.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.connectionsetup_port_label)
        ###2.KISIM###
        self.tabWidget = QtWidgets.QTabWidget(self.MQTTsetup)
        self.tabWidget.setGeometry(QtCore.QRect(10, 100, 241, 201))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sekme_pub = QtWidgets.QWidget()###SEKME Publish
        self.palette = self.tab_sekme_pub.palette()
        self.palette.setColor (QPalette.Window,QColor(0,100,10))
        self.tab_sekme_pub.setPalette(self.palette)
        self.tab_sekme_pub.setAutoFillBackground(True)
        self.tab_sekme_pub.setObjectName("tab_sekme_pub")
        self.publish_linedit = QtWidgets.QLineEdit(self.tab_sekme_pub)
        self.publish_linedit.setEnabled(True)
        self.publish_linedit.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.publish_linedit.setWhatsThis("")
        self.publish_linedit.setAccessibleDescription("")
        self.publish_linedit.setInputMask("")
        self.publish_linedit.setClearButtonEnabled(False)
        self.publish_linedit.setObjectName("publish_linedit")
        self.listWidget = QtWidgets.QListWidget(self.tab_sekme_pub)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 121, 121))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_sekme_pub)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(130, 40, 83, 61))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_pub = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_pub.setContentsMargins(0, 0, 0, 0)
        self.formLayout_pub.setObjectName("formLayout_pub")
        self.publish_add_pushButton = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.publish_add_pushButton.setObjectName("publish_add_pushButton")
        self.formLayout_pub.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.publish_add_pushButton)
        self.publish_remove_pushButton = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.publish_remove_pushButton.setObjectName("publish_remove_pushButton")
        self.formLayout_pub.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.publish_remove_pushButton)
        self.tabWidget.addTab(self.tab_sekme_pub, "")
        self.tab_sekme_sub = QtWidgets.QWidget()###SEKME Subscribe#yerdeğisti!!!pub-*sub-düzenlenmedi
        self.palette = self.tab_sekme_sub.palette()
        self.palette.setColor (QPalette.Window,QColor(0,10,110))
        self.tab_sekme_sub.setPalette(self.palette)
        self.tab_sekme_sub.setAutoFillBackground(True)
        self.tab_sekme_sub.setObjectName("tab_sekme_sub")
        self.subscribe_linedit = QtWidgets.QLineEdit(self.tab_sekme_sub)
        self.subscribe_linedit.setGeometry(QtCore.QRect(10, 10, 191, 20))
        self.subscribe_linedit.setObjectName("subscribe_linedit")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab_sekme_sub)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(130, 40, 83, 61))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_sub = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_sub.setContentsMargins(0, 0, 0, 0)
        self.formLayout_sub.setObjectName("formLayout_sub")
        self.subscribe_add_pushButton = QtWidgets.QPushButton(self.formLayoutWidget_4)
        self.subscribe_add_pushButton.setObjectName("subscribe_add_pushButton")
        self.formLayout_sub.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subscribe_add_pushButton)
        self.subscribe_remove_pushButton = QtWidgets.QPushButton(self.formLayoutWidget_4)
        self.subscribe_remove_pushButton.setObjectName("subscribe_remove_pushButton")
        self.formLayout_sub.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subscribe_remove_pushButton)
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_sekme_sub)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 40, 121, 121))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        #self.tabWidget.addTab(self.tab_sekme_sub, "")  ----Sekme pasif

        ###3.KISIM###
        self.groupBox_events = QtWidgets.QGroupBox(self.MQTTsetup)
        self.groupBox_events.setGeometry(QtCore.QRect(280, 110, 240, 190))
        self.groupBox_events.setObjectName("groupBox_events")
        self.palette = self.groupBox_events.palette()
        self.palette.setColor (QPalette.Window,QColor(222,0,0))
        self.groupBox_events.setPalette(self.palette)
        self.groupBox_events.setAutoFillBackground(True)
        self.events_textBrowser = QtWidgets.QTextBrowser(self.groupBox_events)
        self.events_textBrowser.setGeometry(QtCore.QRect(10, 20, 220, 160))
        self.events_textBrowser.setObjectName("events_textBrowser")

        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self.MQTTsetup)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MQTTsetup", "MQTT Setup"))
        self.groupBox.setTitle(_translate("MQTTsetup", "CONNECTION SETUP"))
        self.label_info.setText(_translate("MQTTsetup","*Only need to press the connect button using the predefined settings*"))
        self.Connect_pushButton.setText(_translate("MQTTsetup", "Connect"))
        self.Disconnect_pushButton.setText(_translate("MQTTsetup", "Disconnect"))
        self.connectionsetup_host_label.setText(_translate("MQTTsetup", "Broker IP"))
        self.connectionsetup_port_label.setText(_translate("MQTTsetup", "PORT"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MQTTsetup", "sensor"))
        item = self.listWidget.item(1)
        item.setText(_translate("MQTTsetup", "location"))
        item = self.listWidget.item(2)
        item.setText(_translate("MQTTsetup", "weather"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.publish_add_pushButton.setText(_translate("MQTTsetup", "OK"))
        self.publish_remove_pushButton.setText(_translate("MQTTsetup", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sekme_pub), _translate("MQTTsetup", "SUBSCRIBE"))
        self.subscribe_add_pushButton.setText(_translate("MQTTsetup", "OK"))
        self.subscribe_remove_pushButton.setText(_translate("MQTTsetup", "Remove"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MQTTsetup", "empty0"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MQTTsetup", "empty1"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sekme_sub), _translate("MQTTsetup", "PUBLISH"))
        self.groupBox_events.setTitle(_translate("MQTTsetup", "EVENTS"))

        self.resize(540, 350)
        self.show()

    def MQTTclient(self, MQTTlayersetupUi):
        if sys.platform == "linux": # for Linux
            os.system("gnome-terminal -e 'python3 MQTTgui.py'")
        elif sys.platform == "win32": # for Windows
            os.system("start cmd /c 'python3 MQTTgui.py'")

    def RSTPlayersetupUi(self):
        """
        Kullanıcı arayüz yapılandırması-RSTPlayer ve sinyal/slot
        """
        self.RSTPlayer_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.RSTPlayer_widget)
        self.setWindowTitle("Stream")

        self.videoframe = QFrame()          #videoframe oluşturduk widget içine alacaz sonra
        self.palette = self.videoframe.palette()
        self.palette.setColor (QPalette.Window,QColor(0,0,0))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)
        self.videoframe.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

        self.hbuttonbox = QHBoxLayout(self)                 #butonlar oluşturuyoruz
        self.streambutton = QPushButton("Launch Stream")  #
        self.hbuttonbox.addWidget(self.streambutton)        #
        self.streambutton.clicked.connect(self.Stream)      #

        self.stopbutton = QPushButton("Stop")               #
        self.hbuttonbox.addWidget(self.stopbutton)          #
        self.stopbutton.clicked.connect(self.Stop)          #

        self.vboxlayout = QVBoxLayout(self)             #Ana pencereye yerleştirmek için
                                                    #vboxlayout tanımladık ve sonra kullandık
        self.vboxlayout.addWidget(self.videoframe)  #VideoFrame ana pencereye eklendi
        self.vboxlayout.addLayout(self.hbuttonbox)  #hbuttonbox ana pencereye eklendi
        #vboxlayout içine koyduk şimdi bunları RSTPlayer_widget'a
        self.RSTPlayer_widget.setLayout(self.vboxlayout)   #dikkat en son rstpwidget a ekledi,RSTPlayer_widget ayarlandı
        #yani enson çuvala koyduk

        self.resize(640, 480)
        self.show()

    def MapLayer(self):
        self.MapLayer_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.MapLayer_widget)
        self.setWindowTitle("MAP")

        self.mapFrame = QFrame(self.MapLayer_widget)
        self.mapFrame.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.mapFrame.setGeometry(QtCore.QRect(10, 10, 500, 500))
        self.palette = self.mapFrame.palette()
        self.palette.setColor (QPalette.Window,QColor(0,220,0))
        self.mapFrame.setPalette(self.palette)
        self.mapFrame.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(self.mapFrame)
        self.label.setGeometry(QtCore.QRect(100, 20, 250, 50))
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
        self.label.setText("BETA***")

        self.MAPbutton = QPushButton(self.MapLayer_widget)#1.BUTON
        self.MAPbutton.setGeometry(QtCore.QRect(250, 510, 50, 50))
        self.MAPbutton.setText("OK")
        self.palette = self.MAPbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(0,220,0))
        self.MAPbutton.setPalette(self.palette)
        self.MAPbutton.setAutoFillBackground(True)
        #self.MAPbutton.clicked.connect(self.)
        self.Xbutton = QPushButton(self.MapLayer_widget)#2.BUTON
        self.Xbutton.setGeometry(QtCore.QRect(200, 510, 50, 50))
        self.Xbutton.setText("X")
        self.palette = self.Xbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(0,220,0))
        self.Xbutton.setPalette(self.palette)
        self.Xbutton.setAutoFillBackground(True)
        self.Ybutton = QPushButton(self.MapLayer_widget)#3.BUTON
        self.Ybutton.setGeometry(QtCore.QRect(250, 560, 50, 50))
        self.Ybutton.setText("Y")
        self.palette = self.Ybutton.palette()
        self.palette.setColor (QPalette.Window,QColor(0,220,0))
        self.Ybutton.setPalette(self.palette)
        self.Ybutton.setAutoFillBackground(True)
        self.Zbutton = QPushButton(self.MapLayer_widget)#4.BUTON
        self.Zbutton.setGeometry(QtCore.QRect(200, 560, 50, 50))
        self.Zbutton.setText("Z")
        self.palette = self.Zbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(0,220,0))
        self.Zbutton.setPalette(self.palette)
        self.Zbutton.setAutoFillBackground(True)#---

        #self.map = QWebView(self)
        #self.openMap = QUrl("http://thomasmansencal.com/Sharing/Others/Google_Maps.html")
		#self.map.load( openMap )
        #self.MapLayer_widget.addWidget( map )

        self.resize(520, 610)
        self.show()

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

    def viewhtml(self):
        import webbrowser
        self.premaps()
        webbrowser.open('where.html')

    def temelmenubar(self):
        """
        Ana ekran menü bar yapılandırılması
        """
        setRSTP = QAction("Setup", self)
        setRSTP.triggered.connect(self.Stream)
        onlyRSTP = QAction("View", self)
        onlyRSTP.triggered.connect(self.RSTPlayersetupUi)

        setMQTT = QAction("Setup", self)
        setMQTT.triggered.connect(self.MQTTlayersetupUi)
        #onlyMQTT = QAction("View", self)
        onlyMQTTsub = QAction("Subscribe", self)
        onlyMQTTpub = QAction("", self)


        setMap = QAction("Setup", self)
        setMap.triggered.connect(self.MapLayer)
        onlyMap = QAction("View", self)
        onlyMap.triggered.connect(self.MapLayer)

        home = QAction("Main Page", self)
        home.triggered.connect(self.MainUi)
        exit = QAction("Exit", self)
        exit.triggered.connect(sys.exit)

        version = QAction("v1.1-beta", self)


        OBEEmenubar = self.menuBar()            #Temel menübar oluşturduk
        General = OBEEmenubar.addMenu("General")
        General.addAction(home)
        General.addSeparator()
        General.addAction(exit)

        RSTPlayermenu = OBEEmenubar.addMenu("RSTP")
        aRSTPmenu = RSTPlayermenu.addAction(onlyRSTP)
        bRSTPmenu = RSTPlayermenu.addAction(setRSTP)

        MQTTlayermenu = OBEEmenubar.addMenu("MQTT")
        aMQTTmenu = MQTTlayermenu.addMenu("View")
        bMQTTmenu = MQTTlayermenu.addAction(setMQTT)
        aaMQTTmenu = aMQTTmenu.addAction(onlyMQTTsub)
        abMQTTmenu = aMQTTmenu.addAction(onlyMQTTpub)

        MapLayermenu = OBEEmenubar.addMenu("Map")
        MapLayermenu.addAction(onlyMap)
        MapLayermenu.addAction(setMap)

        About = OBEEmenubar.addMenu("About")
        About.addAction(version)

    def Stream(self, streambutton):
        """
        play/pause geçiş yapılandırması
        """
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.streambutton.setText("Live")
            self.isPaused = True

        else:
            if self.mediaplayer.play() == -1:
                self.OpenFile()
                return
            self.mediaplayer.play()
            self.streambutton.setText("Pause")
            self.isPaused = False

    def Stop(self):#stop yapılandırması
        self.mediaplayer.stop()
        self.streambutton.setText("BROADCASTING")

    def OpenFile(self,filename=None):
        """
        Yürütülen media yapılandırması
        """
        if filename is None:
            filename = QFileDialog.getOpenFileName(self, "Dosya Seç", os.path.expanduser('~'))[0]
        if not filename:
            return

        # media oluşturuyoruz
        if sys.version < '3':
            filename = unicode(filename)
        self.media = self.instance.media_new(filename)
        # MediaPlayer içine koyalım
        self.mediaplayer.set_media(self.media)

        # Dosyamızın metadata verilerini ayrıştıyoruz
        self.media.parse()

        """
            MediaPlayer QFrame ye bağlı olması gerekiyor:
            Bu durum OS tipine göre değişkenlik göstereceğinden;
            ilgili komutları oluşturuyoruz:)
            Bu olmazsa player katmanı ana pencerede olmuyor:( *5 satır*
        """
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        self.Stream()

    def Event(self):#düzenlenecek
        self.Events_widget = QtWidgets.QWidget(self)
        self.setWindowTitle("Events")

        self.eventsFrame = QFrame(self.Events_widget)
        self.eventsFrame.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.palette = self.eventFrame.palette()
        self.palette.setColor (QPalette.Window,QColor(0,0,0))
        self.eventsFrame.setPalette(self.palette)
        self.eventsFrame.setAutoFillBackground(True)

        self.eventss_textBrowser = QtWidgets.QTextBrowser(self.Events_widget)
        self.eventss_textBrowser.setGeometry(QtCore.QRect(10, 20, 580, 600))

        self.eventsbutton = QPushButton(self.Events_widget)#1.BUTON
        self.eventsbutton.setGeometry(QtCore.QRect(510, 20, 50, 50))
        self.eventsbutton.setText("Events")
        self.palette = self.eventsbutton.palette()
        self.palette.setColor (QPalette.Window,QColor(220,0,0))
        self.eventsbutton.setPalette(self.palette)
        self.eventsbutton.setAutoFillBackground(True)
        #self.eventbutton.clicked.connect(self.Stream)

        self.resize(600, 700)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    a = obeeUi()

    sys.exit(app.exec_())
