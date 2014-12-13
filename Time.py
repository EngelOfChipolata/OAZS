__author__ = 'guilhem'
import _thread
import time
from Tools import *
import random
import sys

IRLTime = 0
IRLTime_begins = time.time()
IGTime_seconds = 19
set_sun = 1
hungry = 4
thirsty = 2
joueur = 0
interrupt = 0
day = 1
OFFSET = 0

def def_joueur(joueur1):
    global joueur
    joueur = joueur1

def igtime():
    global IRLTime
    global IRLTime_begins
    global IGTime_seconds
    global set_sun
    global hungry
    global thirsty
    global joueur
    global OFFSET
    IGTime_seconds = (time.time()-IRLTime_begins)*60 + 10*3600 + OFFSET
    time.sleep(1)
    if time.gmtime(IGTime_seconds)[4] == 0 or time.gmtime(IGTime_seconds)[4] == 30:
        joueur.hungry -=1
    if 8 <= time.gmtime(IGTime_seconds)[3] <= 11 and set_sun != 1:     #Gestion du soleil
        writeinf("The sun is rising.")
        set_sun = 1
    if 12 <= time.gmtime(IGTime_seconds)[3] <= 19 and set_sun != 2:
        writeinf("The sun is high.")
        set_sun = 2
    if 20 <= time.gmtime(IGTime_seconds)[3]<= 23 and set_sun != 3:
        writeinfper("The sun is setting.")
        set_sun = 3
    if 0 <= time.gmtime(IGTime_seconds)[3] <= 7 and set_sun != 0:
        set_sun = 0
        _thread.start_new(midnight,())
    if joueur.hungry <=0 and hungry != 0:         #Gestion de la faim
        write('You died from starvation.')
        hungry = 0
    if 76 <= joueur.hungry <=100 and hungry !=4:
        write('You aren\'t hungry. What a luck !')
        sys.stdout.flush()
        hungry = 4
    if 51 <= joueur.hungry <=75 and hungry !=3:
        write('You wouldn\'t mind having a bite of something.')
        sys.stdout.flush()
        hungry = 3
    if 26 <= joueur.hungry <=50 and hungry !=2:
        write('You are hungry... ')
        sys.stdout.flush()
        hungry = 2
    if 1 <= joueur.hungry <=25 and hungry !=1:
        write('Your stomach is hurting you and you feel dizzy. ')
        sys.stdout.flush()
        hungry = 1
    igtime()


def midnight():
    global interrupt
    global day
    interrupt = 1
    write('A tremendous zombies horde is passing')
    sys.stdout.flush()
    time.sleep(2)
    if joueur.location != [0, 0]:
        write('You have chosen to stay outside, you died.')
        sys.exit()
    else:
        write('.')
    day +=1
    interrupt = 0




# print(time.strftime("%H:%M:%S", time.gmtime(Time.IGTime_seconds)))



# def punchline():
#     time.sleep(5)
#     print('MOO')
#
# _thread.start_new_thread(punchline, ())
# input("interrupting cow")


# montemps=time.time()
# while(True):
#     y=time.time()-montemps
    # print(time.strftime('%M # %S ',time.localtime()))

# while 1:
#     a= random.randint(-5,5)
#     print(a)
#     time.sleep(1)