from .window import Window


def main() -> None:
    print("Opening Window")

    window = Window("Maze Solver!", 800, 600)
    window.wait_for_close()

    print("Shut down!")


if __name__ == "__main__":
    main()
