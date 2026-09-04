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
