__author__ = 'guilhem'
from Player import *
from World import *
from Message import *
from Tools import *
import sys
import time
import Time
import Fight
import Ui

map1 = map
ui = 0
Fighting_Class = None
Command_list = []
Attack_list = []
Command_index = 0


def saisie(joueur, UI2, Fighting):
    global ui
    global Fighting_Class
    global Command_list
    global Command_index
    global Attack_list
    Fighting_Class = Fighting
    ui = UI2
    message = str(ui.playerinput.text())
    if message == "":
        return
    write("<html><head/><body><p><span style=\" font-style:italic; color:#1fad00;\">", message, "</span></p></body></html>")
    Command_index = 0
    ui.playerinput.setText('')
    term = ui.terminal.text()
    word = message[0:].split(' ')
    if Fighting.Combat_Mode == 0:
        Command_list.append(message)
        Attack_list = []
        if Time.interrupt ==1:
            write('You are too scared to do something.')
        elif 'inventory' in message:
            if message.index('inventory') == 0:
                display_inventory(joueur)
            else:
                not_recognize(message)
        elif 'go' in message or 'walk' in message or 'run' in message or 'move' in message:
            if message.index('go') == 0 or message.index('walk') == 0 or message.index('run') == 0 or message.index('move') == 0:
                move(joueur, word)
            else:
                not_recognize(message)
        elif 'eat' in message:
            if message.index('eat') == 0:
                eat(joueur, word)
            else:
                not_recognize(message)
        elif 'quit' in message:
            if len(word) == 1:
                quit2()
            else:
                not_recognize(message)
        elif 'day' in message:
            if len(word) == 1:
                dsp_day()
            else:
                not_recognize(message)
        elif 'time' in message:
            if len(word) == 1:
                dsp_time()
            else:
                not_recognize(message)
        elif 'unequip' in message or 'unwear' in message:
            if message.index('unequip') == 0 or message.index('unwear') == 0:
                unequip(joueur, word)
            else:
                not_recognize(message)
        elif 'equipment' in message:
            if message.index('equipment') == 0:
                equipment(joueur)
            else:
                not_recognize(message)
        elif 'equip' in message:
            if message.index('equip') == 0:
                equip(joueur, word)
            else:
                not_recognize(message)
        else:
            not_recognize(message)
    else:
        Attack_list.append(message)
        if 'attack' in message:
            Fighting_Class.attack(joueur)
            Fighting_Class.fight_global(joueur)

        elif 'equip' in message:
            if message.index('equip') == 0:
                equip(joueur, word)
                Fighting_Class.tour += 1
                Fighting_Class.fight_global(joueur)
            else:
                not_recognize(message)

def display_inventory(joueur):
    if len(joueur.inventory) == 0:
        write('You have nothing... Woe is you')
    else:
        for i in range(0,len(joueur.inventory)):
            write(joueur.inventory[i].name)


def eat(joueur, word):
    if len(word)==1:
        write('What do you want to eat ?')
    elif word[1] in dict_item:
        if len(joueur.inventory)==0:
                write('You have nothing to eat.')
        elif dict_item[word[1]].gainhungry != 0 and joueur.hungry != 100:
                for i in range(0, len(joueur.inventory)):
                    if str(word[1]) == joueur.inventory[i].tag:
                        write('This', joueur.inventory[i].tag, 'tastes weird, but your stomach thanks you.')
                        joueur.hungry += joueur.inventory[i].gainhungry
                        if joueur.hungry > 100:
                            joueur.hungry = 100
                        joueur.inventory[i:i+1] = []
                        break
                    elif i == len(joueur.inventory)-1:
                        write('You don\'t have any', word[1], 'to eat.')
        elif dict_item[word[1]].gainHP != 0 and joueur.HP != 100:
                for i in range(0, len(joueur.inventory)):
                    if str(word[1]) == joueur.inventory[i].tag:
                        write('This', joueur.inventory[i].tag, 'makes you feel better.')
                        joueur.HP += joueur.inventory[i].HP
                        joueur.inventory[i:i+1] = []
                        break
                    elif i == len(joueur.inventory)-1:
                        write('You don\'t have any', word[1], 'to eat.')
        else:
            write('You can\'t eat', word[1], '!')
    else:
        write('I don\'t know what', word[1], 'is.')


def move(joueur, word):
    list_mvt = ['go', 'walk', 'run', 'move']
    if len(word)==1:
        write('Where you wanna go ?')
    elif word[1]== 'north':
        if (joueur.location[0],joueur.location[1]+1) in World.map:
            joueur.hungry -= 10
            Time.OFFSET += 1*3600
            joueur.location[1] +=1
            wait_points(3)
            write(World.map[tuple(joueur.location)].description)
            writeinfper(World.map[tuple(joueur.location)].name)
            write(enemy_count(tuple(joueur.location))[0])
        else:
            write('You can\'t go there.')
    elif word[1] == 'south':
        if (joueur.location[0],joueur.location[1]-1) in World.map:
            joueur.hungry -= 10
            Time.OFFSET += 1*3600
            joueur.location[1] -=1
            wait_points(3)
            write(World.map[tuple(joueur.location)].description)
            writeinfper(World.map[tuple(joueur.location)].name)
            write(enemy_count(tuple(joueur.location))[0])
        else:
            write('You can\'t go there.')
    elif word[1] == 'east':
        if (joueur.location[0]+1,joueur.location[1]) in World.map:
            joueur.hungry -= 10
            Time.OFFSET += 1*3600
            joueur.location[0] +=1
            wait_points(3)
            write(World.map[tuple(joueur.location)].description)
            writeinfper(World.map[tuple(joueur.location)].name)
            write(enemy_count(tuple(joueur.location))[0])
        else:
            write('You can\'t go there.')
    elif word[1] == 'west':
        if (joueur.location[0]-1,joueur.location[1]) in World.map:
            joueur.hungry -= 10
            Time.OFFSET += 1*3600
            joueur.location[0] -=1
            wait_points(3)
            write(World.map[tuple(joueur.location)].description)
            writeinfper(World.map[tuple(joueur.location)].name)
            write(enemy_count(tuple(joueur.location))[0])
        else:
            write('You can\'t go there.')
    else :
        write('You can\'t go', word[1])
    if enemy_count(tuple(joueur.location))[1] != 0:
        weak = enemy_count(tuple(joueur.location))[1]-1
        write('A', str(World.map[tuple(joueur.location)].monstersin['Weak '+str(weak)].tag)[:-1], 'runs furiously toward you')
        Fighting_Class.fight(joueur, World.map[tuple(joueur.location)].monstersin['Weak '+str(weak)])
    if enemy_count(tuple(joueur.location))[2] != 0:
        common = enemy_count(tuple(joueur.location))[1]-1
        write('A', str(World.map[tuple(joueur.location)].monstersin['Common '+str(common)].tag)[:-1], 'runs furiously toward you')
        Fight.fight(joueur, World.map[tuple(joueur.location)].monstersin['Common '+str(common)])
    if enemy_count(tuple(joueur.location))[2] != 0:
        heavy = enemy_count(tuple(joueur.location))[1]-1
        write('A', str(World.map[tuple(joueur.location)].monstersin['Heavy '+str(heavy)].tag)[:-1], 'runs furiously toward you')
        Fight.fight(joueur, World.map[tuple(joueur.location)].monstersin['Heavy '+str(heavy)])


def equip(joueur,word):
    if len(word)==1:
        write('What do you want to equip ?')
    elif word[1] in dict_item:
        if len(joueur.inventory) == 0:
            display_inventory(joueur)
        else:
            for i in range(0, len(joueur.inventory)):
                if str(word[1]) in joueur.inventory[i].tag:
                    if dict_item[word[1]].defense !=-1:
                        write('You wear', word[1], ', it suits you !')
                        joueur.inventory[i:i+1] = []
                        if joueur.defenseeqpd != '':
                            joueur.inventory.append(joueur.defenseeqpd)
                        joueur.defenseeqpd = dict_item[word[1]]
                        break
                    elif dict_item[word[1]].attack !=-1:
                        write('You hold', word[1], 'and you will not hesitate to use it !')
                        joueur.inventory[i:i+1] = []
                        if joueur.attackeqpd != '':
                            joueur.inventory.append(joueur.attackeqpd)
                        joueur.attackeqpd = dict_item[word[1]]
                        break
                    else:
                        write(word[1], 'is not equipable.')
                        break
                elif i == len(joueur.inventory)-1:
                    write('You don\'t have any', word[1], 'to equip.')
    else:
        write('I don\'t know what', word[1], 'is.')


def equipment(joueur):
    if joueur.defenseeqpd != '':
        write('You are wearing', joueur.defenseeqpd.name, '.')
    else :
        write('You are almost naked. Shame on you.')
    if joueur.attackeqpd != '':
        write('\nYou are holding', joueur.attackeqpd.name, '.')
    else :
        write('You have nothing in your hands.')


def unequip(joueur,word):
    if joueur.defenseeqpd=='' and joueur.attackeqpd=='':
        write('You have nothing to unequip !')
    elif len(word) == 1:
        write('What do you want to unequip ?')
    elif word[1]==joueur.defenseeqpd.name or word[1]==joueur.defenseeqpd.tag or word[1]=='defense':
        write('You feel lighter.')
        joueur.inventory.append(joueur.defenseeqpd)
        joueur.defenseeqpd = ''
    elif word[1] == joueur.attackeqpd.name or word[1]==joueur.attackeqpd.tag or word[1]=='weapon':
        write('You feel lighter.')
        joueur.inventory.append(joueur.attackeqpd)
        joueur.attackeqpd = ''
    else:
        write(word[1], 'is not equiped.')


def dsp_time():
    write('By watching the sun you can tell it\'s', time.strftime("%H", time.gmtime(Time.IGTime_seconds)))


def dsp_day():
    write('You can bearly remember... You think is day', int(Time.IGTime_seconds/86400) + 1)


def not_recognize(message):
    write(message + ' is not a descent command.')


def call(a):
    global Command_list
    global Command_index
    global Attack_list
    global ui
    l = [Command_list, Attack_list][Fighting_Class.Combat_Mode]
    if l != []:
        Command_index += a
        if Command_index <= 0:
           Command_index = 1
        if Command_index > len(l):
             Command_index = len(l)
        ui.playerinput.setText(l[-Command_index])


def quit2():
    write('Good Bye !')
    slept(2)
    quit()