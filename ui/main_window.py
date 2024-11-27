import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget
from components.video_player import VideoPlayer


class videoSorterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.folder_path = ""
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Video Sorter')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.folder_button = QPushButton('Select Folder')
        self.folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_button)

        self.video_list = QListWidget()
        self.video_list.itemDoubleClicked.connect(self.play_video)
        layout.addWidget(self.video_list)

        self.video_player = VideoPlayer(self)
        layout.addWidget(self.video_player.video_widget)

        self.setLayout(layout)

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if self.folder_path:
            self.load_videos(self.folder_path)
    

    def load_videos(self, folder_path):
        self.video_list.clear()
        for file in os.listdir(folder_path):
            if file.endswith('.mp4'):
                self.video_list.addItem(os.path.join(folder_path, file))

    def play_video(self, item):
        video_path = os.path.join(self.folder_path, item.text())
        self.video_player.play(video_path)