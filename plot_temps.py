#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.artist as ma
import itertools as it

def format_he10_data(fname):
    d = np.loadtxt(fname, usecols=(1, 8, 9, 10))
    dates = [dt.datetime.fromtimestamp(t) for t in d[:,0]]
    temps = [d[:,1], d[:,2], d[:,3]]
    return dates, temps

def plot_he10_data(ax, dates, temps):
    lines = ['-', '--', '-.']
    linecycler = it.cycle(lines)
    label = ['He3U Head', 'He3I Head', 'He4 Head']
    labelcycler = it.cycle(label)
    for temp in temps:
        ax.plot(dates, temp, next(linecycler), label=next(labelcycler))
