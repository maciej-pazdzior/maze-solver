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
        point1 = Point(x1, y1)
        point2 = Point(x2, y1)
        point3 = Point(x1, y2)
        point4 = Point(x2, y2)
        if self.has_left_wall:
            self._win.draw_line(Line(point1, point3))
        if self.has_right_wall:
            self._win.draw_line(Line(point2, point4))
        if self.has_top_wall:
            self._win.draw_line(Line(point1, point2))
        if self.has_bottom_wall:
            self._win.draw_line(Line(point3, point4))
