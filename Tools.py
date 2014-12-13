__author__ = 'guilhem'
import World
import sys
import _thread
import time
import Ui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtTest import *


UI = None


def enemy_count(u):
    weak = 0
    common = 0
    heavy = 0
    message = 'You see '
    for i in range(len(World.map[u].monstersin)):
        if 'Weak '+str(i) in World.map[u].monstersin:
            weak += 1
        if 'Common '+str(i) in World.map[u].monstersin:
            common += 1
        if 'Heavy '+str(i) in World.map[u].monstersin:
            heavy += 1
    if weak != 0:
        message += str(weak)+' weak zombies'
        if common != 0 or heavy != 0:
            message += ', and '
    if common !=0:
        message += str(common)+' common zombies'
        if heavy !=0:
            message + ', and '
    if heavy != 0:
        message += str(heavy)+' heavy zombies'
    if weak == 0 and common == 0 and heavy == 0:
        message += 'no enemies... What a luck'
    message += '.'
    if u == (0, 0):
        message = 'Home sweet home'
    return [message, weak, common, heavy]


def wait_points(time_sec):
        time_sec_3 = int(time_sec/3)
        for i in range(3):
            write('.')
            slept(time_sec_3)
        return



def Gset(ui):
    global UI
    UI = ui


def write(message1, message2 = "", message3 = "", message4="", message5="", message6="", message7="", message8="", message9="",message10=""):
    global UI
    actual = UI.terminal.text()
    list=[message1,message2,message3,message4,message5,message6,message7,message8,message9,message10]
    i = 0
    display = actual+'<html><head/><body><p>'
    while list[i]!= "":
        display += str(list[i])
        display += str(" ")
        i+=1
    UI.terminal.setText(display+'</p></body></html>')

def writeinf(message1, message2 = "", message3 = "", message4="", message5="", message6="", message7="", message8="", message9="",message10=""):
    global UI
    former=UI.infos.text()
    UI.infos.setText(message1+message2+message3+message4+message5+message6+message7+message8+message9+message10)
    time.sleep(4)
    UI.infos.setText(former)



def writeinfper(message, message2 = "", message3 = "", message4="", message5="", message6="", message7="", message8="", message9="",message10=""):
    _thread.start_new_thread(writeinfpermthread, (message, message2, message3, message4, message5, message6, message7, message8, message9, message10))

def writeinfpermthread(message, message2 = "", message3 = "", message4="", message5="", message6="", message7="", message8="", message9="",message10=""):
    global UI
    UI.infos.setText(message+message2+message3+message4+message5+message6+message7+message8+message9+message10)


def slept(a):
    QTest.qWait(100)
    QTest.qSleep(a*1000-100)