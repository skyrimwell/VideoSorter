from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class VideoPlayer(QVideoWidget):
    def __init__(self, parent):
        self.video_widget = QVideoWidget(parent)
        self.video_widget.setMinimumSize(640, 360)
        self.video_widget.show()
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)


    def play(self, video_path):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.player.play()