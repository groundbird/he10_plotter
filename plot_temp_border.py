#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plot_temps
import sys
import datetime as dt
import itertools as it
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.artist as ma

def main():
    if len(sys.argv) == 1: f = 'data/he10_2013_1225_214621.dat'
    else: f = sys.argv[1]
    dates, temps = plot_temps.format_he10_data(f)
    # plot
    fig = plt.figure()
    ax = plt.subplot(111)
    plot_temps.plot_he10_data(ax, dates, temps)
    ax.axvline(x=dt.datetime(2014, 1, 10, 21, 7), lw=2, color='black')
    # range
    xmin = dt.datetime(2014, 1, 10, 19)
    xmax = dt.datetime(2014, 1, 10, 23)
    ax.set_xlim(xmin, xmax)
    # tune
    ax.grid()
    xfmt = md.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    ax.set_ylabel('Temperature [K]', fontsize=15)
    ax.legend(loc='upper center', ncol=3)
    ax.set_ylim(0, 1)
    plt.savefig('data/border.eps')
    plt.show()

if __name__ == '__main__':
    main()
