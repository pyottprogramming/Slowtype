# -*- coding: utf-8 -*-

from game_functions import diatype, slowtype, breakline

def yesno():
    yeslist = ["Yes", "Yes.", "yes", "yes.", "y", "y."]
    nolist = ["No", "No.", "no", "no.", "n", "n."]
    global response
    if answer in yeslist:
        response = 1
    if answer in nolist:
        response = 2
    return;

diatype(dialogue = "Greetings Adventurer!What's your name?")
Playername = input()
diatype(dialogue = "Well, hello " + Playername + "!")
slowtype(dialogue = "You attempt to open your eyes but shut them against a blinding light. You hear a faint, dry laugh.")
diatype(dialogue = "Ah, eager to start are we?")
answer = input()
yesno()
if response == 1:
    pass
if response == 2:
    diatype("No?Well, unfortunately, we're running out of time to convince you, so.")
slowtype("The light fades into a cold blackness, a creeping sensation of air rushing past envelops you. You are in freefall.")
