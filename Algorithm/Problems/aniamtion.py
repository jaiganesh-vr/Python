import numpy as np
from Lib import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Forest:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.trees = np.zeros((self.height, self.width, 3), dtype=np.uint8) #uint since you are using 3D arrays
        self.images = []

    def simulate(self, iterations):
        # for i in range(iterations):
        #     for j in range(self.height):
        #         for k in range(self.width):
        #             #some logic goes here
        for i in range(iterations):
            self.trees = np.random.randint(0, 255, (self.height, self.width, 3), dtype=np.uint8)
            self.images.append([plt.imshow(self.trees / 255, animated=True)]) # add the [] since it needs to be iterable

    def update_fig(self, j):
        global im
        im = self.images[j]
        return im


f = 0.000005
p = 0.01

forest = Forest(100, 100)
forest.simulate(500)

fig = plt.figure()
im = forest.images[0]
ani = animation.FuncAnimation(fig, forest.update_fig, interval=50, blit=True)
plt.show()