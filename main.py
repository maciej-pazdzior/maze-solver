from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(250, 250, 500, 500)
    win.wait_for_close()


if __name__ == "__main__":
    main()