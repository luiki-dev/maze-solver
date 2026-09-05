from .drawables import Line, Point, Window


def main() -> None:
    print("Opening Window")

    window = Window("Maze Solver!", 800, 600)

    line1: Line = Line(Point(10, 150), Point(50, 200))
    line2: Line = Line(Point(190, 40), Point(60, 210))

    window.draw_line(line1, "black")
    window.draw_line(line2, "red")

    window.wait_for_close()

    print("Shut down!")


if __name__ == "__main__":
    main()
