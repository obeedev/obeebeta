import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, QVBoxLayout, QAction, QFileDialog, QApplication

class MQTTlayer(QMainWindow):
    def __init__(self, master=None):
        QMainWindow.__init__(self, master)
        self.setWindowTitle("MQTT Telemetry Screen")

        self.MQTTgui()

    def MQTTgui(self):
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
        #self.setWindowTitle(_translate("MQTTsetup", "MQTT Setup"))
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
        import paho.mqtt.client as mqtt
        from store_Sensor_Data_to_DB import sensor_Data_Handler

        def on_connect(client, userdata, flags, rc):
            print("bağlanıldı"+ "" +str(rc))

            """bağlantıya abone olundu >>on_connect()
            eğerki bağlantı kaoparsa abonelik üzerinden yeniden bağlantı sağlanır"""
            #Burada 2 abonelik konusu var, yayıncı bu konularda ne gönderirse alır
            client.subscribe("weather")
            client.subscribe("sensor")
            client.subscribe("location")

        #sunucudan geridönüş>> *yayın alındığında
        def on_message(client, userdata, msg):
            print ("MQTT Data Received...")
            print ("MQTT Topic: " + msg.topic)
            print ("Data: " + str(msg.payload))
            sensor_Data_Handler(msg.topic, msg.payload)



        #şimdi MQTT Client(istemci) oluşturarak rutinler ekleyelim
        client = mqtt.Client()
        db = sensor_Data_Handler
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("test.mosquitto.org", 1883, 60)

        client.loop_forever()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    a = MQTTlayer()

    sys.exit(app.exec_())
