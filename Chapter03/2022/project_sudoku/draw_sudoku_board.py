from typing import NamedTuple
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams["font.weight"] = "bold"
plt.rcParams.update({'mathtext.default':  'default'})
plt.rcParams.update({'font.size': 28})


class Position(NamedTuple):
    xpos: int
    ypos: int


if __name__ == "__main__":
    sudoku = [[8, 3, 9, 6, 5, 7, 2, 1, 4], 
              [6, 7, 2, 9, 4, 1, 5, 8, 3],
              [1, 5, 4, 8, 3, 2, 9, 6, 7], 
              [5, 4, 1, 2, 8, 3, 7, 9, 6],
              [2, 8, 7, 4, 9, 6, 3, 5, 1], 
              [9, 6, 3, 7, 1, 5, 4, 2, 8], 
              [7, 1, 8, 3, 2, 9, 6, 4, 5], 
              [3, 2, 5, 1, 6, 4, 8, 7, 9], 
              [4, 9, 6, 5, 7, 8, 1, 3, 2]]

    sudoku_title: str = "solution"    
    sudoku_size: int = 9
    lb: Position = Position(0, 0)
    rb: Position = Position(sudoku_size, 0)
    lt: Position = Position(0, sudoku_size)

    plt.figure(figsize=(9, 9))
    for i in range(0, (sudoku_size + 1)):
        plt.plot([lb.xpos, rb.xpos], [lb.ypos + i, rb.ypos + i], 'k')
        plt.plot([lb.xpos + i, lt.xpos + i], [lb.ypos, lt.ypos], 'k')
    
    for i in range(0, sudoku_size):
        for j in range(0, sudoku_size):
            plt.text(i + 0.4, j + 0.4, str(sudoku[(sudoku_size - 1) - i][j]))
    
    # plt.title(sudoku_title)
    plt.axis('off')
    plt.savefig('sudoku_board.png')
    plt.close()
    