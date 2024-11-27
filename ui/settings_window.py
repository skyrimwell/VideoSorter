# ui/settings_window.py
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFileDialog, QHBoxLayout

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Folder Settings')
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()
        self.folder_entries = []


        self.add_folder_entry(layout)

        layout.addStretch()

        add_button = QPushButton('+ Add folder')
        add_button.clicked.connect(lambda: self.add_folder_entry(layout))
        layout.addWidget(add_button)

        save_button = QPushButton('Save')
        save_button.clicked.connect(self.save_folders)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def add_folder_entry(self, layout):
        folder_layout = QHBoxLayout()

        folder_name_input = QLineEdit()
        folder_name_input.setPlaceholderText('Название папки')
        folder_layout.addWidget(folder_name_input)

        folder_path_input = QLineEdit()
        folder_path_input.setPlaceholderText('Путь к папке')
        folder_layout.addWidget(folder_path_input)

        browse_button = QPushButton('...')
        browse_button.clicked.connect(lambda: self.select_folder(folder_path_input))
        folder_layout.addWidget(browse_button)

        layout.insertLayout(0, folder_layout)

        self.folder_entries.insert(0, (folder_name_input, folder_path_input))


    def select_folder(self, path_input):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select folder')
        if folder_path:
            path_input.setText(folder_path)

    def save_folders(self):
        for folder_name_input, folder_path_input in self.folder_entries:
            folder_name = folder_name_input.text().strip()
            folder_path = folder_path_input.text().strip()

            if folder_name and folder_path:
                full_path = os.path.join(folder_path, folder_name)
                if not os.path.exists(full_path):
                    os.makedirs(full_path)
