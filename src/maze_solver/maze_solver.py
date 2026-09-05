from maze_solver.maze import Maze

from .drawables import Window

CELL_SIZE = 50
START_X = 25
START_Y = 25


def main() -> None:
    print("Opening Window")

    window = Window("Maze Solver!", 800, 600)

    maze: Maze = Maze(START_X, START_Y, 11, 15, CELL_SIZE, CELL_SIZE, window)

    solved = maze.solve()

    print(f"Maze {'' if solved else 'NOT '}solved!")

    window.wait_for_close()

    print("Shut down!")


if __name__ == "__main__":
    main()
