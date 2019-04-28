
from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser
import numpy as np

# changeable arguements for invoking code in command-line
parser = ArgumentParser(description="Branching")
parser.add_argument('--nodes', '-n', default='5', type=int)
parser.add_argument('--length', '-l', default='1', type=float)
parser.add_argument('--ratio', '-r', default='0.6', type=float)
parser.add_argument('--offset', '-o', default='0.1', type=float)
arguments = parser.parse_args()


def run(nodes, length, offset, ratio, plot=True):
    each_node = 0
    current_branches = np.array([[0, length, 0]])  # initalise the first branch

    if plot == True:
        # plots the first branch
        plt.plot([0, current_branches[0][0]], [0, current_branches[0][1]])

    # loops over every branching point
    while each_node < nodes:

        # extracts all the coordinates and separates them
        all_x = current_branches[:, 0]
        all_y = current_branches[:, 1]
        all_angles = current_branches[:, 2]

        # calcualte branching angles in different directions separately
        angle_left = all_angles - offset
        angle_right = all_angles + offset

        # calculate coordinates for left branching
        x_left = all_x + length * np.sin(angle_left)
        y_left = all_y + length * np.cos(angle_left)

        # calculate coordinates for right branching
        x_right = all_x + length * np.sin(angle_right)
        y_right = all_y + length * np.cos(angle_right)

        # combine x & y coordinates and the corresponding angle together for
        # each direction
        new_left = np.dstack((x_left, y_left, angle_left))
        new_right = np.dstack((x_right, y_right, angle_right))

        if plot == True:
            # plots left and right branches separately
            plt.plot([all_x, x_left], [all_y, y_left])
            plt.plot([all_x, x_right], [all_y, y_right])

        # reset starting branches for the next branching
        current_branches = np.vstack((new_left[0], new_right[0]))

        # change length for next branching
        length *= ratio

        # move the loop on to the next branching
        each_node += 1

    if plot == True:
        plt.savefig('tree_np.png')  # generate graph


if __name__ == "__main__":
    run(arguments.nodes, arguments.length,
        arguments.offset, arguments.ratio)
