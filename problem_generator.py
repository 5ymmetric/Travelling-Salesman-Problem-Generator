# Author: Karthik Reddy Pagilla

from random import randrange, uniform
import matplotlib.pyplot as plt

class Point:
    def __init__(self, X, Y, index):
        self.index = index
        self.X = X
        self.Y = Y
        self.parent = None

    def toString(self):
        return "X : " + str(self.X) + ", Y: " + str(self.Y)

class ProblemGenerator:
    def __init__(self, size):
        self.size = size
        self.points = []

        index = 0
        index += 1
        point = Point(uniform(0, 1), uniform(0, 1), index)
        self.points.append(point)
        prevPoint = point

        while(len(self.points) < self.size):
            index += 1
            point = Point(uniform(0, 1), uniform(0, 1), index)
            prevPoint.parent = point
            if (point not in self.points):
                self.points.append(point)
                prevPoint = point

    def plot(self):
        X = [point.X for point in self.points]
        Y = [point.Y for point in self.points]

        plt.scatter(X, Y)

        for point in self.points:
            plt.annotate(point.index, xy=(point.X, point.Y), xytext=(-5, -5), textcoords='offset points', ha='right', va='bottom')

            if point.parent is not None:
                plt.plot([point.X, point.parent.X], [point.Y, point.parent.Y], c='r', linewidth=2)
        
        plt.show()

problem = ProblemGenerator(17)

problem.plot()