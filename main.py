from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QLabel


def win_check(grid) -> None | str:
    # check each row
    # check each col
    # check diags
    return None


def reset(board, text_label):
    for row in board:
        for box in row:
            box.setText("")
    text_label.setText("Current Turn: X")


def main():
    # ui setup
    app = QApplication()
    window = QWidget(windowTitle="PyTacToe")
    v_layout = QVBoxLayout(window)
    top_text = QLabel("Current Turn: X")
    v_layout.addWidget(top_text)
    grid_layout = QGridLayout()
    v_layout.addLayout(grid_layout)
    boxes = [[QPushButton("") for _ in range(3)] for _ in range(3)]
    for r, row in enumerate(boxes):
        for c, box in enumerate(row):
            box.setFixedSize(100, 100)
            grid_layout.addWidget(box, r, c)
    bottom_bar = QHBoxLayout()
    reset_button = QPushButton("Reset Board")
    reset_button.clicked.connect(lambda: reset(boxes, top_text))
    bottom_bar.addWidget(reset_button)
    exit_button = QPushButton("Exit Game")
    exit_button.clicked.connect(app.quit)
    bottom_bar.addWidget(exit_button)
    v_layout.addLayout(bottom_bar)
    window.show()
    app.exec()

    current_player = "X"


if __name__ == "__main__":
    main()
