#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from __future__ import print_function # Needed by the progress bar
import logging

import numpy as np

def is_sublist(sl, ll):
    findex=0
    eindex=0

    for i in range(len(ll)):
        if ll[i]==sl[eindex]: 
            if eindex==0: findex=i
            eindex+=1
        else: eindex=0

        if eindex==len(sl): return findex

    return -1

def merge_arrays(a, b):
    if len(a) != len(b):
        return None
    #assert len(a) == len(b), "Can not merge arrays with different lenght."

    tlen=(len(a)+len(b))
    c=[None]*tlen

    for i in range(0, tlen, 2):
        if i/2 < len(a): c[i]=a[i/2]
        if i/2 < len(b): c[i+1]=b[i/2]

    return c

def pretty_print(content, title):
    result = ""
    WIDTH = 100
    side=(WIDTH-4-len(title))/2
    if len(title)%2 == 0: 
        offs=2
    else: 
        offs=1

    result += "+"+"-"*int(side-offs) + "[ " + title + " ]" + "-"*int(side) + "+\n"
    result += "|"+" "*int(WIDTH-2)+"|\n"
    content = content.split("\n")

    for line in content:
        pline = "|  " + line + " "*int(WIDTH-4-len(line))+"|"
        result += pline+"\n"

    result += "+"+"-"*int(WIDTH-2)+"+\n"
    return result

def print_iterations(iterations):
    outtext=""
    for loop in range(len(iterations)):
        outtext+="CLUSTER {0}\n".format(loop)

        for it in iterations[loop]:
            outtext+="> Iteration_1 found @ [{0} ,{1})\n"\
                    .format(it[0], it[1])

    pretty_print(outtext, "Random iterations by cluster")


class Printer():
    def __init__(self,data):                     
        sys.stdout.write("\x1b[K"+data.__str__())
        sys.stdout.flush()

class ProgressBar(object):
    def __init__(self, msg, total):
        self.total = total
        self.progression = 0
        self.bar_size=20
        self.msg_size=20
        self.update_every=2
        self.count = 0
        self.msg = msg
        self.last_percent = 0

        if len(self.msg) > self.msg_size:
            self.msg = self.msg[:self.msg_size-4]+"... "
        else:
            self.msg = self.msg + " "*(self.msg_size-len(self.msg))
        self.show()

    def progress_by(self, by):
        self.progression += by
        self.show()

    def show(self):
        percent = (self.progression*100)/self.total
        if percent - self.last_percent < self.update_every \
            or self.progression == self.total\
            or self.progression == 0:

            self.last_percent = percent
            pbar_syms = (self.progression*self.bar_size)/self.total
            pbar_spac = self.bar_size-pbar_syms

            if self.progression == self.total:
                endc="\n"
            else:
                endc="\r"

            print("{0} [{1}>{2}] {3}%  {4}/{5}".format(
                self.msg,
                "="*int(pbar_syms),
                " "*int(pbar_spac), 
                str(round(percent,2)), 
                str(self.progression),
                str(self.total)), end=endc)
            self.count = 0
