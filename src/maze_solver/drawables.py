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
