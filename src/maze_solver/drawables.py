from tkinter import BOTH, Canvas, Tk


class Window:
    __root: Tk
    __canvas: Canvas
    __running: bool

    def __init__(self, title: str, width: int, height: int) -> None:
        self.__root: Tk = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    __start_point: Point
    __end_point: Point

    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.__start_point = start_point
        self.__end_point = end_point

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.__start_point.x,
            self.__start_point.y,
            self.__end_point.x,
            self.__end_point.y,
            fill=fill_color,
            width=2,
        )


class Cell:
    has_left_wall: bool
    has_right_wall: bool
    has_top_wall: bool
    has_bottom_wall: bool
    __left_x: int
    __rigth_x: int
    __top_y: int
    __bottom_y: int
    __win: Window | None

    def __init__(self, window: Window | None = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__left_x = -1
        self.__rigth_x = -1
        self.__top_y = -1
        self.__bottom_y = -1
        self.__win = window

    def draw(self, top_left: Point, bottom_right: Point) -> None:
        self.__left_x = top_left.x
        self.__rigth_x = bottom_right.x
        self.__top_y = top_left.y
        self.__bottom_y = bottom_right.y

        top_right = Point(self.__rigth_x, self.__top_y)
        bottom_left = Point(self.__left_x, self.__bottom_y)

        if self.__win != None:
            if self.has_left_wall:
                self.__win.draw_line(Line(top_left, bottom_left), "black")
            if self.has_right_wall:
                self.__win.draw_line(Line(top_right, bottom_right), "black")
            if self.has_top_wall:
                self.__win.draw_line(Line(top_left, top_right), "black")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(bottom_left, bottom_right), "black")

    def draw_move(self, target_cell: Cell, undo: bool = False) -> None:
        center = Point(
            (self.__left_x + self.__rigth_x) // 2,
            (self.__top_y + self.__bottom_y) // 2,
        )
        target_center = Point(
            (target_cell.__left_x + target_cell.__rigth_x) // 2,
            (target_cell.__top_y + target_cell.__bottom_y) // 2,
        )

        if self.__win != None:
            fill_color = "grey" if undo else "red"
            self.__win.draw_line(Line(center, target_center), fill_color)
