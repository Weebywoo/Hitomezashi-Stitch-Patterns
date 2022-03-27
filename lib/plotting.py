import matplotlib.pyplot as plt
import numpy as np


def plotting(lines_x_dir: np.ndarray, lines_y_dir: np.ndarray) -> None:
    fig, ax = plt.subplots()

    for y, y_line in enumerate(lines_x_dir):
        for index in range(y_line, lines_y_dir.shape[0], 2):
            plt.plot([y, y], [index, index + 1], "b-")

    for x, x_line in enumerate(lines_y_dir):
        for index in range(x_line, lines_x_dir.shape[0], 2):
            plt.plot([index, index + 1], [x, x], "b-")

    plt.show()
