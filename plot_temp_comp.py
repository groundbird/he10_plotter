#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plot_temps
import sys
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.artist as ma
import itertools as it
        
def main():
    if len(sys.argv) == 1: f = 'data/he10_2013_1225_214621.dat'
    else: f = sys.argv[1]
    d1 = plot_temps.format_he10_data(f)
    d2 = plot_temps.format_he10_data(f)
    # plot
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 2), (0, 0))
    ax2 = plt.subplot2grid((1, 2), (0, 1))
    plot_temps.plot_he10_data(ax1, *d1)
    plot_temps.plot_he10_data(ax2, *d2)
    # range
    x1min = dt.datetime(2014, 1, 1)
    x1max = dt.datetime(2014, 1, 8)
    x2min = dt.datetime(2014, 1, 11)
    x2max = dt.datetime(2014, 1, 18)
    ax1.set_xlim(x1min, x1max)
    ax2.set_xlim(x2min, x2max)
    # tune
    ax1.grid()
    ax1.grid(which='minor')
    ax2.grid()
    ax2.grid(which='minor')
    ax1.semilogy()
    ax2.semilogy()
    plt.subplots_adjust(wspace=0.05)
    ax1.set_ylabel('Temperature [K]', fontsize=15)
    ma.setp(ax2.get_yticklabels(), visible=False)
    daysLoc1 = md.DayLocator(interval=2)
    daysLoc2 = md.DayLocator(interval=2)
    ax1.xaxis.set_major_locator(daysLoc1)
    ax2.xaxis.set_major_locator(daysLoc2)
    plt.legend(ncol=3, bbox_to_anchor=[0.92, 1.0])
    xfmt = md.DateFormatter('%b.%d')
    ax1.xaxis.set_major_formatter(xfmt)
    ax2.xaxis.set_major_formatter(xfmt)
    ax1.set_title('Rotation with 20 rpm', fontsize=15)
    ax2.set_title('No rotaion', fontsize=15)
    plt.savefig("eps/comp_temps.eps")
    plt.show()

if __name__ == '__main__':
    main()
