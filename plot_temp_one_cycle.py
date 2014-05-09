#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plot_temp_comp
import sys
import datetime as dt
import itertools as it
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.artist as ma

def main():
    if len(sys.argv) == 1: f = 'data/he10_2013_1225_214621.dat'
    else: f = sys.argv[1]
    dates, temps = plot_temp_comp.format_he10_data(f)
    # plot
    fig = plt.figure()
    ax = plt.subplot(111)
    plot_temp_comp.plot_he10_data(ax, dates, temps)
    # range
    xmin = dt.datetime(2014, 1, 1, 18)
    xmax = dt.datetime(2014, 1, 3, 3)
    ax.set_xlim(xmin, xmax)
    # tune
    ax.grid()
    ax.grid(which='minor')
    ax.semilogy()
    xfmt = md.DateFormatter('%b.%d\n%H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    ax.set_ylabel('Temperature [K]', fontsize=15)
    hoursLoc = md.HourLocator(interval=6)
    ax.xaxis.set_major_locator(hoursLoc)
    ax.legend(loc='upper center', ncol=3)
    plt.savefig('eps/one_cycle.eps')
    plt.show()

if __name__ == '__main__':
    main()
