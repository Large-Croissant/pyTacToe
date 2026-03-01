from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


def main():
    app = QApplication()
    window = QWidget(windowTitle="PyTacToe")
    window.setFixedSize(350, 350)
    grid_layout = QGridLayout(parent=window)
    window.show()
    boxes = [[QPushButton() for _ in range(3)] for _ in range(3)]
    for r, row in enumerate(boxes):
        for c, box in enumerate(row):
            box.setFixedSize(100, 100)
            grid_layout.addWidget(box, r, c)
    app.exec()


if __name__ == "__main__":
    main()
