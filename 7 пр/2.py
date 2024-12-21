import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox
from PyQt6.QtGui import QAction  
from PyQt6.QtCore import QFileInfo

class NotesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")
        self.setGeometry(100, 100, 700, 500)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.current_file = None
        self.create_menu()

    def create_menu(self):
        file_menu = self.menuBar().addMenu("Файл")

        new_note_action = QAction("Новая заметка", self, shortcut="Ctrl+N", triggered=self.new_note)
        file_menu.addAction(new_note_action)

        save_note_action = QAction("Сохранить заметку", self, shortcut="Ctrl+S", triggered=self.save_note)
        file_menu.addAction(save_note_action)

    def new_note(self):
        self.text_edit.clear()
        self.current_file = None
        self.setWindowTitle("Новая заметка")

    def save_note(self):
        if not self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)")
            if file_path:
                self.current_file = file_path
        if self.current_file:
            self.write_to_file(self.current_file)

    def write_to_file(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
            self.setWindowTitle(f"Заметка - {QFileInfo(file_path).fileName()}")
            QMessageBox.information(self, "Успех", "Заметка успешно сохранена!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при сохранении файла: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec())
