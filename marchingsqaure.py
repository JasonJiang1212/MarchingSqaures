# coding:utf-8
from matplotlib import pylab
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


class PlotDemo:
    def __init__(self, m, n):
        self._net = None
        self.m = m
        self.n = n

    def _set_default_figure(self, m, n):
        ax = subplot(111)
        xmajorLocator = MultipleLocator(10)
        xmajorFormatter = FormatStrFormatter('%1.1f')
        xminorLocator = MultipleLocator(1)
        ymajorLocator = MultipleLocator(10)
        ymajorFormatter = FormatStrFormatter('%1.1f')
        yminorLocator = MultipleLocator(1)
        ax.set_xlim(0, m)
        ax.set_ylim(0, n)
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.xaxis.set_major_formatter(xmajorFormatter)
        ax.yaxis.set_major_locator(ymajorLocator)
        ax.yaxis.set_major_formatter(ymajorFormatter)
        ax.xaxis.set_minor_locator(xminorLocator)
        ax.yaxis.set_minor_locator(yminorLocator)
        ax.xaxis.grid(True, which='minor')
        ax.yaxis.grid(True, which='minor')

    def show_source(self):
        self._set_default_figure(self.m, self.n)

        if self._net is None:
            raise Exception
        net = self._net.net_info
        shape = net.shape
        xlen = shape[0]
        ylen = shape[1]
        for i in range(xlen):
            for j in range(ylen):
                if net[i][j] > 0:
                    plot(i, j, 'g+')
        show()

    def show_contour(self):
        self._set_default_figure(self.m, self.n)
        net = self._net.net_info
        shape = net.shape
        xlen = shape[0]
        ylen = shape[1]
        for i in range(xlen):
            for j in range(ylen):
                if net[i][j] > 0:
                    plot(i, j, 'g+')

        net = self._net
        utils = MarchSquareUtlis(net)
        lines = utils.trancing_contours()

        width, height = net.net_info.shape
        arr = net.net_info
        idx = 0
        for i in range(width - 1):
            for j in range(height - 1):
                x, y = i, j
                count, v1, v2, v3, v4, v5, v6, v7, v8 = lines[idx]
                idx = idx + 1
                if count == 0:
                    continue
                if count == 1:
                    x1 = x + v1
                    y1 = y + v2
                    x2 = x + v3
                    y2 = y + v4
                    plot(x1, y1, x2, y2, 'ro')
                if count == 2:
                    x1 = x + v1
                    y1 = y + v2
                    x2 = x + v3
                    y2 = y + v4
                    plot(x1, y1, x2, y2, 'ro')
                    x1 = x + v5
                    y1 = y + v6
                    x2 = x + v7
                    y2 = y + v8
                    plot(x1, y1, x2, y2, 'ro')
        show()

    def set_net_info(self, net_info):
        self._net = net_info


class RandomGenNet(object):

    def __init__(self):
        self.arr = self._gen_random()

    def __init__(self, m, n):
        self.arr = self._gen_random(m, n)

    @property
    def net_info(self):
        return self.arr

    def _gen_random(self, m=100, n=100):
        return np.zeros((m, n), dtype='double')

    def add_circle(self, center_x, center_y, radius, val):
        r = int(radius + 0.5)
        for x in range(center_x - r, center_x + r):
            rx = np.abs(center_x - x)
            ry = int(np.sqrt(radius * radius - rx * rx))
            for y in range(ry):
                self.arr[x][center_y - y] = val
                self.arr[x][center_y + y] = val
        return

    def add_retangle(self, lf_up_x, lf_up_y, width, height, val):
        for i in range(width):
            for j in range(height):
                self.arr[lf_up_x + i][lf_up_y + j] = val



def get_retangle_bit(v1, v2, v3, v4):
    return v1 << 3 | v2 << 2 | v3 << 1 | v4



def get_retangle_shift(bitval):
    if bitval == 0 or bitval == 15:
        return (0, None, None, None, None, None, None, None, None)
    if bitval == 1 or 14:
        return (1, 0, 0.5, 0.5, 1, None, None, None, None)
    if bitval == 2 or bitval == 13:
        return (1, 0.5, 1, 1, 0.5, None, None, None, None)
    if bitval == 3 or bitval == 12:
        return (1, 0, 0.5, 1, 0.5, None, None, None, None)
    if bitval == 4 or bitval == 11:
        return (1, 0, 0.5, 1, 0.5, None, None, None, None)
    if bitval == 5:
        return (2, 0, 0.5, 0.5, 0, 0.5, 1, 1, 0.5)
    if bitval == 6 or bitval == 9:
        return (1, 0.5, 0, 0.5, 1, None, None, None, None)
    if bitval == 7 or bit == 8:
        return (1, 0, 0.5, 0.5, 0, None, None, None, None)
    if bitval == 10:
        return (2, 0, 0.5, 0.5, 1, 0.5, 0, 1, 0.5)


class MarchSquareUtlis(object):

    def __init__(self, net):
        self.net = net

    def trancing_contours(self):
        ret = []
        width, height = self.net.net_info.shape
        arr = self.net.net_info
        for i in range(width - 1):
            for j in range(height - 1):
                v1 = int(arr[i][j])
                v2 = int(arr[i + 1][j])
                v3 = int(arr[i + 1][j + 1])
                v4 = int(arr[i][j + 1])
                bitv = get_retangle_bit(v1, v2, v3, v4)
                net_shift = get_retangle_shift(bitv)
                ret.append(net_shift)
        return ret


demo = PlotDemo(100, 100)
netinfo = RandomGenNet(100, 100)
netinfo.add_circle(20, 20, 10, 1)
netinfo.add_circle(70, 50, 20, 1)
netinfo.add_circle(70, 30, 20, 1)
netinfo.add_retangle(20, 45, 40, 20, 1)
netinfo.add_retangle(60, 10, 20, 70, 1)

demo.set_net_info(netinfo)
demo.show_contour()
# print get_retangle_bit(1, 1, 1, 0)
# print range(3)
