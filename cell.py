from graphics import Point, Line

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        point1 = Point(self._x1, self._y1)
        point2 = Point( self._x2, self._y1)
        point3 = Point(self._x1, self._y2)
        point4 = Point( self._x2, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(point1, point3))
        if self.has_right_wall:
            self._win.draw_line(Line(point2, point4))
        if self.has_top_wall:
            self._win.draw_line(Line(point1, point2))
        if self.has_bottom_wall:
            self._win.draw_line(Line(point3, point4))

    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "grey"
        point1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        point2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        self._win.draw_line(Line(point1, point2), fill_color)
        