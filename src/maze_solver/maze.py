import random
import time

from maze_solver.drawables import Cell, Point, Window
from maze_solver.utils import Direction


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
        seed: int | None = None,
    ) -> None:
        self.__position_x = position_x
        self.__position_y = position_y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        if seed != None:
            random.seed()

        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)
        self.__reset_cells_visited()

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

            time.sleep(0.02)

    def __break_entrance_and_exit(self) -> None:
        c = 0
        r = 0

        self.__cells[c][r].has_top_wall = False
        self.__draw_cell(c, r)

        c = self.__num_cols - 1
        r = self.__num_rows - 1

        self.__cells[c][r].has_bottom_wall = False
        self.__draw_cell(c, r)

    def __break_walls(self, c, r) -> None:
        cell: Cell = self.__cells[c][r]
        cell.visited = True

        while True:
            directions_to_visit: dict[Direction, tuple[int, int]] = {}

            # check left
            if c > 0:
                left_cell: Cell = self.__cells[c - 1][r]
                if not left_cell.visited:
                    directions_to_visit[Direction.LEFT] = (c - 1, r)

            # check right
            if c < self.__num_cols - 1:
                right_cell: Cell = self.__cells[c + 1][r]
                if not right_cell.visited:
                    directions_to_visit[Direction.RIGHT] = (c + 1, r)

            # check top
            if r > 0:
                top_cell: Cell = self.__cells[c][r - 1]
                if not top_cell.visited:
                    directions_to_visit[Direction.TOP] = (c, r - 1)

            # check bottom
            if r < self.__num_rows - 1:
                bottom_cell: Cell = self.__cells[c][r + 1]
                if not bottom_cell.visited:
                    directions_to_visit[Direction.BOTTOM] = (c, r + 1)

            # finish if nowhere to go
            if len(directions_to_visit) == 0:
                self.__draw_cell(c, r)
                return

            chosen_direction: Direction = random.choice(  # nosec B311
                list(directions_to_visit.keys())
            )

            # Break adjecent walls
            direction: tuple[int, int] = directions_to_visit[chosen_direction]
            goto_cell: Cell = self.__cells[direction[0]][direction[1]]

            match chosen_direction:
                case Direction.LEFT:
                    cell.has_left_wall = False
                    goto_cell.has_right_wall = False
                case Direction.RIGHT:
                    cell.has_right_wall = False
                    goto_cell.has_left_wall = False
                case Direction.TOP:
                    cell.has_top_wall = False
                    goto_cell.has_bottom_wall = False
                case Direction.BOTTOM:
                    cell.has_bottom_wall = False
                    goto_cell.has_top_wall = False

            self.__break_walls(direction[0], direction[1])

    def __reset_cells_visited(self) -> None:
        for c in self.__cells:
            for cell in c:
                cell.visited = False

    def solve(self) -> bool:
        return self.__solve(0, 0)

    def __solve(self, c: int, r: int) -> bool:
        self.__animate()

        cell: Cell = self.__cells[c][r]
        cell.visited = True

        if c == self.__num_cols - 1 and r == self.__num_rows - 1:
            # end cell reached
            return True

        if self.__visit_adjecent_cell(cell, Direction.LEFT, c > 0, c - 1, r):
            return True

        if self.__visit_adjecent_cell(
            cell, Direction.RIGHT, c < self.__num_cols - 1, c + 1, r
        ):
            return True

        if self.__visit_adjecent_cell(cell, Direction.TOP, r > 0, c, r - 1):
            return True

        return self.__visit_adjecent_cell(
            cell, Direction.BOTTOM, r < self.__num_rows - 1, c, r + 1
        )

    def __visit_adjecent_cell(
        self,
        cell: Cell,
        direction: Direction,
        edge_condition_met: bool,
        target_c: int,
        target_r: int,
    ) -> bool:
        if not cell.has_wall(direction) and edge_condition_met:
            target_cell: Cell = self.__cells[target_c][target_r]
            if not target_cell.visited:
                cell.draw_move(target_cell)

                if self.__solve(target_c, target_r):
                    return True

                cell.draw_move(target_cell, undo=True)

        return False
