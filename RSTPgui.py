import os
import sys
import VLC
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, QVBoxLayout, QAction, QFileDialog, QApplication

class RSTPlayer(QMainWindow):
    def __init__(self, master = None):
        QMainWindow.__init__(self, master)
        self.setWindowTitle("RSTP Real-Time Streaming Screen")

        self.instance = VLC.Instance()
        self.mediaplayer = self.instance.media_player_new()

        self.RSTPgui()
        self.isPaused = False

    def RSTPgui(self):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    a = RSTPlayer()

    sys.exit(app.exec_())
