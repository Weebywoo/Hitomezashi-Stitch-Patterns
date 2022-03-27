import numpy as np
from hitomezashi_stitch_patterns.lib.plotting import plotting


def main() -> None:
    size = (50, 50)
    lines_x_dir = np.random.randint(0, 2, size[0])
    lines_y_dir = np.random.randint(0, 2, size[1])

    plotting(lines_x_dir, lines_y_dir)


if __name__ == '__main__':
    main()
