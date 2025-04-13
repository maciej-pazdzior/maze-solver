from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 12, 16, 50, 50, win)
    maze._create_cells()
    win.wait_for_close()


if __name__ == "__main__":
    main()