from typing import NamedTuple
import matplotlib.pyplot as plt


class Position(NamedTuple):
    xpos: int
    ypos: int


if __name__ == "__main__":
    sudoku_size = 9
    lb: Position = Position(0, 0)
    rb: Position = Position(sudoku_size, 0)
    lt: Position = Position(0, sudoku_size)

    plt.figure(figsize=(9, 9))
    for i in range(0, (sudoku_size + 1)):
        plt.plot([lb.xpos, rb.xpos], [lb.ypos + i, rb.ypos + i], 'k')
        plt.plot([lb.xpos + i, lt.xpos + i], [lb.ypos, lt.ypos], 'k')
    
    plt.show()