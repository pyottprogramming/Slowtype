# -*- coding: utf-8 -*-

import sys, time

def diatype(dialogue):
    diacount = 0
    punctuationlist = [".", "!", "?"]
    dialength = len(dialogue)
    sys.stdout.write("'")
    sys.stdout.flush()
    time.sleep(.05)
    while dialength != diacount:
        sys.stdout.write(dialogue[diacount])
        sys.stdout.flush()
        if dialogue[diacount] == ",":
            time.sleep(.1)
        elif dialogue[diacount] in punctuationlist:
            sys.stdout.write("'")
            sys.stdout.flush()
            time.sleep(.05)
            if diacount < dialength - 1:
                sys.stdout.write("\n" + "'")
                sys.stdout.flush()
                time.sleep(.05)
        else:
            time.sleep(.05)
        diacount += 1
    if dialength == diacount:
        sys.stdout.write("\n")
        sys.stdout.flush()
    return;

def slowtype(dialogue):
    diacount = 0
    dialength = len(dialogue)
    while dialength != diacount:
        sys.stdout.write(dialogue[diacount])
        sys.stdout.flush()
        time.sleep(.02)
        if dialogue[diacount] == ",":
            time.sleep(.05)
        diacount += 1
    if dialength == diacount:
        sys.stdout.write("\n")
        sys.stdout.flush()
    return;    

def breakline():
    sys.stdout.write("\n")
    sys.stdout.flush()