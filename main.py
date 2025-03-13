import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent

class Mouse_Tracking(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week 3 : F1D022049 - I Nengah Dwi Putra W.")
        self.setGeometry(100, 100, 1000, 1000)
        
        self.mouse_kordinat_label = QLabel(self)
        self.mouse_kordinat_label.setGeometry(10, 10, 280, 30)
        self.mouse_kordinat_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mouse_kordinat_label.setText("Mouse Kordinat: (0, 0)")
        self.mouse_kordinat_label.setStyleSheet("background-color: lightgray; padding: 5px;")
        
        self.setMouseTracking(True)
        self.mouse_kordinat_label.setMouseTracking(True)
        self.mouse_kordinat_label.show()

    def mouseMoveEvent(self, event: QMouseEvent):
        x = event.x()
        y = event.y()
        
        self.mouse_kordinat_label.setText(f"Mouse Kordinat: ({x}, {y})")
        self.mouse_kordinat_label.update()
        
        label_rect = self.mouse_kordinat_label.geometry()
        if label_rect.contains(x, y):
            self.move_label_randomly()

    def move_label_randomly(self):
        window_width = self.width()
        window_height = self.height()
        label_width = self.mouse_kordinat_label.width()
        label_height = self.mouse_kordinat_label.height()

        max_x = window_width - label_width
        max_y = window_height - label_height
        
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        
        self.mouse_kordinat_label.move(new_x, new_y)

def main():
    app = QApplication(sys.argv)
    window = Mouse_Tracking()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()