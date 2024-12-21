import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример сигналов и слотов')
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel('Нажмите кнопку', self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button = QPushButton('Нажми меня', self)

        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.apply_styles("black", "red", "20px", "18px")

    def apply_styles(self, label_color, button_color, label_size, button_size):
        self.label.setStyleSheet(f"color: {label_color}; font-size: {label_size};")
        self.button.setStyleSheet(f"background-color: {button_color}; font-size: {button_size};")

    def on_button_click(self):
        self.label.setText('Кнопка нажата!')
        # Изменение стиля после нажатия
        self.apply_styles("red", "grey", "24px", "20px")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
