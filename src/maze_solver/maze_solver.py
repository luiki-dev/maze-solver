import random

from .drawables import Cell, Point, Window

CELL_SIZE = 50


def main() -> None:
    print("Opening Window")

    window = Window("Maze Solver!", 800, 600)

    for _ in range(4):
        left_x = random.randint(0, 800 - CELL_SIZE)
        top_y = random.randint(0, 600 - CELL_SIZE)

        cell = Cell(window)
        cell.has_left_wall = random.choice([True, False])
        cell.has_right_wall = random.choice([True, False])
        cell.has_top_wall = random.choice([True, False])
        cell.has_bottom_wall = random.choice([True, False])

        cell.draw(
            Point(left_x, top_y),
            Point(left_x + CELL_SIZE, top_y + CELL_SIZE),
        )

    window.wait_for_close()

    print("Shut down!")


if __name__ == "__main__":
    main()
