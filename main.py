from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from dataclasses import dataclass


@dataclass
class Gamestate:
    current_turn: str = "X"
    top_label: QLabel = None
    boxes: list[list[QPushButton]] = None


def boxes_enabled(gamestate: Gamestate, enabled: bool):
    for row in gamestate.boxes:
        for box in row:
            box.setEnabled(enabled)


def win_check(gamestate: Gamestate) -> None | str:
    # check each row
    for i in range(3):
        if gamestate.boxes[i][0].text() == gamestate.boxes[i][1].text() == gamestate.boxes[i][2].text() != "":
            return gamestate.boxes[i][0].text()
    # check each col
    for i in range(3):
        if gamestate.boxes[0][i].text() == gamestate.boxes[1][i].text() == gamestate.boxes[2][i].text() != "":
            return gamestate.boxes[0][i].text()
    # check diags
    if gamestate.boxes[0][0].text() == gamestate.boxes[1][1].text() == gamestate.boxes[2][2].text() != "":
        return gamestate.boxes[0][0].text()
    if gamestate.boxes[0][2].text() == gamestate.boxes[1][1].text() == gamestate.boxes[2][0].text() != "":
        return gamestate.boxes[0][2].text()
    return None


def reset(gamestate: Gamestate):
    for row in gamestate.boxes:
        for box in row:
            box.setText("")
    gamestate.current_turn = "X"
    gamestate.top_label.setText(f"Current Turn: {gamestate.current_turn}")
    boxes_enabled(gamestate, True)


def do_turn(gamestate: Gamestate, r, c):
    box = gamestate.boxes[r][c]
    if box.text() == "":
        box.setText(gamestate.current_turn)
        gamestate.current_turn = "X" if gamestate.current_turn == "O" else "O"
        gamestate.top_label.setText(f"Current Turn: {gamestate.current_turn}")
        winner = win_check(gamestate)
        if winner is not None:
            gamestate.top_label.setText(f"WINNER: {winner}\nCONGRADULATIONS!")
            boxes_enabled(gamestate, False)


def main():
    gamestate = Gamestate()
    # ui setup
    app = QApplication()
    window = QWidget(windowTitle="PyTacToe")
    v_layout = QVBoxLayout(window)
    top_text = QLabel(f"Current Turn: {gamestate.current_turn}")
    v_layout.addWidget(top_text)
    gamestate.top_label = top_text
    grid_layout = QGridLayout()
    v_layout.addLayout(grid_layout)
    boxes = [[QPushButton("") for _ in range(3)] for _ in range(3)]
    for r, row in enumerate(boxes):
        for c, box in enumerate(row):
            box.setFixedSize(100, 100)
            grid_layout.addWidget(box, r, c)
            box.clicked.connect(lambda _, r=r, c=c: do_turn(gamestate, r, c))
    gamestate.boxes = boxes
    bottom_bar = QHBoxLayout()
    reset_button = QPushButton("Reset Board")
    reset_button.clicked.connect(lambda: reset(gamestate))
    bottom_bar.addWidget(reset_button)
    exit_button = QPushButton("Exit Game")
    exit_button.clicked.connect(app.quit)
    bottom_bar.addWidget(exit_button)
    v_layout.addLayout(bottom_bar)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
