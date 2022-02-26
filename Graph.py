import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
from statistics import stdev

# bar graph
# pie graph
params = {'xtick.labelsize': 'x-large',
          'ytick.labelsize': 'x-large'}
pylab.rcParams.update(params)


class Modifier:
    def add_modification(self):
        pass


class AverageLines(Modifier):
    def __init__(self, ax, average, x, y):
        self.ax = ax
        self.x = x
        self.y = y
        if average == (None, None):
            self.y_mean = [np.mean(self.y)] * len(self.y)
            self.x_mean = [np.mean(self.x)] * len(self.x)
        else:
            self.y_mean = [(average[1])] * len(self.y)
            self.x_mean = [(average[0])] * len(self.x)

    def add_modification(self):
        self.ax.plot(self.x, self.y_mean, label='Mean', color='red')
        self.ax.plot(self.x_mean, self.y, label='Mean', color='red')


class InvertY(Modifier):
    def __init__(self):
        pass

    def add_modification(self):
        plt.gca().invert_yaxis()


class InvertX(Modifier):
    def __init__(self):
        pass

    def add_modification(self):
        plt.gca().invert_xaxis()


class DiagonalLines(Modifier):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.x = x
        self.y = y

    def add_modification(self):
        x_sdev = stdev(self.x)
        y_sdev = stdev(self.y)
        y_list, x_list = [], []
        ymid = (self.ax.get_ylim()[0] + self.ax.get_ylim()[1]) / 2
        xmid = (self.ax.get_xlim()[0] + self.ax.get_xlim()[1]) / 2
        ysteps = abs((self.ax.get_ylim()[1] - self.ax.get_ylim()[0]) // (y_sdev / 2))
        xsteps = abs((self.ax.get_xlim()[1] - self.ax.get_xlim()[0]) // (x_sdev))
        # print(int(0 - (ysteps / 2)), int(0 + (ysteps / 2)))
        for i in range(int(0 - (ysteps / 2)), int(0 + (ysteps / 2))):
            y_list.append(ymid + (i * y_sdev))
        for i in range(int(0 - (xsteps / 2)), int(0 + (xsteps / 2))):
            x_list.append(xmid + (i * x_sdev))
        x_list.append(x_list[-1] + x_sdev)
        # print(y_list)
        slope = (y_list[0] - y_list[-1]) / (min(x_list) - max(x_list))
        for pointx in x_list:
            # plt.scatter(x=pointx, y=ymid, color='blue')
            plt.axline((pointx, ymid), slope=slope, color='gray')


class BestFit(Modifier):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_modification(self):
        plt.plot(np.unique(self.x), np.poly1d(np.polyfit(self.x, self.y, 1))(np.unique(self.x)), color='green')


class PointLabels(Modifier):
    def __init__(self, ax, x, y, labels):
        self.ax = ax
        self.x = x
        self.y = y
        self.labels = labels

    def add_modification(self):
        for index in range(0, len(self.x)):
            self.ax.annotate(self.labels[index], (self.x[index], self.y[index]), textcoords="offset points", ha='center', xytext=(0, -25))


class Labels(Modifier):
    def __init__(self, ax, x, y, labels):
        self.ax = ax
        self.x = x
        self.y = y
        self.labels = labels

    def add_modification(self):
        for index in range(0, len(self.x)):
            image = OffsetImage(plt.imread(self.labels[index]), zoom=.40)
            self.ax.autoscale()
            ab = AnnotationBbox(image, (self.x[index], self.y[index]), frameon=False)
            self.ax.add_artist(ab)


class Dots(Modifier):
    def __init__(self, ax, x, y, label=''):
        self.ax = ax
        self.x = x
        self.y = y
        self.label = label

    def add_modification(self):
        self.ax.scatter(self.x, self.y, label=self.label)


class Graph2DScatter:
    def __init__(self, x, y, labels, axis_labels, average_lines=True, inverty=False, invertx=False, size=(12.2, 12), diag_lines=True, best_fit=False, dot_labels=None, average=(None, None),
                 multiple_x=None, x_ticks=None, xaxis=None, yaxis=None):
        self.modifiers = []
        self.x = x
        self.y = y
        self.fig = plt.figure(figsize=size)
        self.ax = self.fig.add_subplot()
        # self.xaxis = xaxis
        # self.yaxis = yaxis
        if multiple_x is None:
            pass
        else:
            years = range(1951, 2020)
            i = 0
            for t in multiple_x[:-1]:
                self.modifiers.append(Dots(self.ax, t, range(1, len(t)+1), label=str(years[i])))
                i += 1
        if x_ticks is not None:
            plt.xticks(x_ticks)
        if not labels:
            self.modifiers.append(Dots(self.ax, self.x, self.y, label='2018'))
        else:
            self.labels = labels
            self.modifiers.append(Labels(self.ax, self.x, self.y, labels))
        if dot_labels is None:
            self.dot_labels = []
        else:
            self.modifiers.append(PointLabels(self.ax, self.x, self.y, dot_labels))
        if average_lines:
            self.modifiers.append(AverageLines(self.ax, average, x=self.x, y=self.y))
        self.axis_labels = axis_labels
        if inverty:
            self.modifiers.append(InvertY())
        if invertx:
            self.modifiers.append(InvertX())
        if diag_lines:
            self.modifiers.append(DiagonalLines(self.ax, self.x, self.y))
        if best_fit:
            self.modifiers.append(BestFit(self.x, self.y))

    def graph(self):
        self.ax.set_xlabel(self.axis_labels[0], fontsize=18)
        self.ax.set_ylabel(self.axis_labels[1], fontsize=18)
        for modifier in self.modifiers:
            modifier.add_modification()
        # if self.xaxis is not None:
        #     plt.ylim([self.yaxis[0], self.yaxis[1]])
        #     plt.xlim([self.xaxis[0], self.xaxis[1]])
        # plt.legend(loc="upper right")
        # plt.margins(0, 0)
        plt.savefig('1', bbox_inches='tight')
        # return plt


class LineGraph:
    def __init__(self, x, y, other_lines=None, labels=None):
        self.x = x
        self.y = y
        self.other_lines = other_lines
        self.labels = labels

    def graph(self):
        plt.plot(self.x, self.y)
        for line in self.other_lines:
            plt.plot(self.x, line)
        plt.legend(self.labels)
        return plt