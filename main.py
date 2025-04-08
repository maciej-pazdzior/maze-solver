from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(250, 250, 500, 500)
    cell2 = Cell(win)
    cell2.draw(250, 500, 500, 750)
    cell1.draw_move(cell2)
    win.wait_for_close()


if __name__ == "__main__":
    main()