
from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


parser = ArgumentParser(description="Branching")
parser.add_argument('--nodes', '-n', default='5', type=int)
parser.add_argument('--length', '-l', default='1', type=float)
parser.add_argument('--ratio', '-r', default='0.6', type=float)
parser.add_argument('--offset', '-o', default='0.1', type=float)
arguments = parser.parse_args()


def branching(branch_list, previous_branch, offset, direction, length):

    if direction == "left":
        angle = previous_branch[2] - offset
    elif direction == "right":
        angle = previous_branch[2] + offset

    new_branch = [previous_branch[0] + length *
                  sin(angle), previous_branch[1] + length * cos(angle), angle]
    branch_list.append(new_branch)


def add_plots(branch_list, previous_branch):
    plt.plot([previous_branch[0], branch_list[-2][0], previous_branch[0], branch_list[-1][0]],
             [previous_branch[1], branch_list[-2][1], previous_branch[1], branch_list[-1][1]])


def run(nodes, length, offset, ratio, plot=True):
    current_branches = [[0, length, 0]]
    if plot:
        plt.plot([0, current_branches[0][0]], [0, current_branches[0][1]])
    for i in range(nodes):
        new_branches = []

        for each_branch in current_branches:
            branching(new_branches, each_branch, offset, "left", length)
            branching(new_branches, each_branch, offset, "right", length)
            if plot:
                add_plots(new_branches, each_branch)

        current_branches = new_branches
        length *= ratio

    if plot:
        plt.savefig('tree.png')

if __name__ == "__main__":
    run(arguments.nodes, arguments.length,
        arguments.offset, arguments.ratio, arguments.plot)
