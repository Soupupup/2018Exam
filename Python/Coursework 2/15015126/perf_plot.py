import timeit
from matplotlib import pyplot as plt


nodes = 1
time = []
iteration = []
# timing no-numpy code generating trees with layers up to 12 and each
# repeated 10000 times
while nodes <= 12:
    time.append(timeit.timeit("run({},1,0.1,0.6,False)".format(
        nodes),  number=1000, setup="from tree import run"))

    iteration.append(nodes)
    nodes += 1
# plotting the final result
plt.plot(iteration, time, '-x', label="No Numpy")

# reset variables for testing numpy version
nodes = 1
time = []
iteration = []
# timing numpy-incorporated code generating trees with layers up to 12 and
# each repeated 10000 times
while nodes <= 12:
    time.append(timeit.timeit("run({},1,0.1,0.6,False)".format(
        nodes),  number=1000, setup="from tree_np import run"))

    iteration.append(nodes)
    nodes += 1
# plotting the final result
plt.plot(iteration, time, '-x', label="With Numpy")

# formatting the graph and generating it as an image
plt.ylabel("Total Run Time (s)")
plt.xlabel("Number of iteration steps taken")
plt.title("Performance test for Numpy")
plt.legend()
plt.savefig('perf_plot.png')
