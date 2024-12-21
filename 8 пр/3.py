import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QFileDialog, QLabel, QSlider
)
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Минималистичный видеоплеер")
        self.setGeometry(100, 100, 800, 600)

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)

        self.file_label = QLabel("Выберите видеофайл", self)
        self.file_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.play_pause_button = QPushButton("Пуск/Пауза", self)
        self.play_pause_button.clicked.connect(self.toggle_play_pause)

        self.open_file_button = QPushButton("Открыть файл", self)
        self.open_file_button.clicked.connect(self.open_file)

        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.update_duration)

        self.media_player.errorOccurred.connect(self.handle_error)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.file_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.play_pause_button)
        layout.addWidget(self.open_file_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите видеофайл", "", "Видео файлы (*.mp4 *.avi *.mkv)")
        if file_path:
            self.file_label.setText(file_path)
            print(f"Открыт файл: {file_path}")
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.media_player.play()
            print(f"Состояние медиаплеера: {self.media_player.playbackState()}")

    def toggle_play_pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def update_slider(self, position):
        self.slider.setValue(position)

    def update_duration(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def handle_error(self, error):
        """Обработка ошибок воспроизведения"""
        print(f"Ошибка воспроизведения: {error}")
        print(f"Описание ошибки: {self.media_player.errorString()}")
        if error != QMediaPlayer.Error.NoError:
            print("Проблема с воспроизведением. Проверьте наличие кодеков или формат файла.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec())
