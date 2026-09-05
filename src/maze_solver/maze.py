import time

from maze_solver.drawables import Cell, Point, Window


class Maze:
    __position_x: int
    __position_y: int
    __num_rows: int
    __num_cols: int
    __cell_size_x: int
    __cell_size_y: int
    __window: Window | None
    __cells: list[list[Cell]]

    def __init__(
        self,
        position_x: int,
        position_y: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window | None = None,
    ) -> None:
        self.__position_x = position_x
        self.__position_y = position_y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        self.__cells = []

        self.__create_cells()

    def __create_cells(self) -> None:
        for c in range(self.__num_cols):
            self.__cells.append([])

            for r in range(self.__num_rows):
                self.__cells[c].append(Cell(self.__window))

                self.__draw_cell(c, r)

    def __draw_cell(self, c: int, r: int) -> None:
        cell: Cell = self.__cells[c][r]

        top_left: Point = Point(
            self.__position_x + c * self.__cell_size_x,
            self.__position_y + r * self.__cell_size_y,
        )
        bottom_right: Point = Point(
            self.__position_x + (c + 1) * self.__cell_size_x,
            self.__position_y + (r + 1) * self.__cell_size_y,
        )

        cell.draw(top_left, bottom_right)

        self.__animate()

    def __animate(self) -> None:
        if self.__window != None:
            self.__window.redraw()

            time.sleep(0.05)
