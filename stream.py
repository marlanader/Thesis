from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QMessageBox)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys

class VideoWindow(QMainWindow):

    def __init__(self, parent=None):
        super(VideoWindow, self).__init__(parent)
        self.setWindowTitle("Live Streaming") 
        self.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.resize(1078,600)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2 = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()
        videoWidget2= QVideoWidget()
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)       
        self.trigger = QPushButton()
        self.trigger.setText("Trigger an alarm")
        self.trigger.clicked.connect(self.confirmation)
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        # Create new action
        

        # Create exit action
        
   

        # Create menu bar and add action
        

        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.trigger)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(videoWidget2)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        # Set widget to contain window contents
        wid.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.error.connect(self.handleError)

        self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile("./video.wmv")))
        self.mediaPlayer2.setVideoOutput(videoWidget2)
        self.mediaPlayer2.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer2.error.connect(self.handleError)

        self.mediaPlayer2.setMedia(
                    QMediaContent(QUrl.fromLocalFile("./video2.wmv")))

       
    def confirmation(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Would you like to trigger an alarm?")
        msgBox.setWindowTitle("Confirmation Message")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            msgBox2=QMessageBox()
            msgBox2.setIcon(QMessageBox.Warning)
            msgBox2.setText("Your request has been reported")
            msgBox2.setWindowTitle("Calling Ambulance...")
            msgBox2.setStandardButtons(QMessageBox.Ok)
            returnValue2 = msgBox2.exec()
    def exitCall(self):
        sys.exit(app.exec_())
    def play(self):
            self.mediaPlayer.play()
            self.mediaPlayer2.play()
         

    def mediaStateChanged(self, state):
        
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    player = VideoWindow()
    player.resize(1078, 632)
    player.show()
    sys.exit(app.exec_())