import time
import random

from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_entrence_and_exit()
        if seed is not None:
            self.seed = random.seed(seed)
        else:
            self.seed = seed
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for row in range(self.num_rows):
            row = []
            for col in range(self.num_cols):
                row.append(Cell(self.win))
            self._cells.append(row)
        for row in self._cells:
            for cell in row:
                i = self._cells.index(row)
                j = row.index(cell)
                self._draw_cell(i, j)
            

    def _draw_cell(self, i, j):
        x1 = self.x1 + self.cell_size_x * j
        x2 = self.x1 + self.cell_size_x * (j + 1)
        y1 = self.y1 + self.cell_size_y * i 
        y2 = self.y1 + self.cell_size_y * (i + 1) 
        self._cells[i][j].draw(x1, y1, x2, y2)
        # self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrence_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit = self._cells[self.num_rows-1][self.num_cols-1]
        exit.has_bottom_wall = False
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
            for d in directions:
                k = i+d[0]
                l = j+d[1]
                if self.num_rows-1 >= k >= 0 and self.num_cols-1 >= l >= 0:
                    if self._cells[k][l].visited == False:
                        to_visit.append((k, l))
            if to_visit == []:
                self._draw_cell(i, j)
                return
            chosen_cell = random.choice(to_visit)
            if chosen_cell[0] > i:
                current_cell.has_bottom_wall = False
            elif chosen_cell[0] < i:
                current_cell.has_top_wall = False
            elif chosen_cell[1] > j:
                current_cell.has_right_wall = False
            elif chosen_cell[1] < j:
                current_cell.has_left_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(chosen_cell[0], chosen_cell[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False



