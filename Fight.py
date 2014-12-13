__author__ = 'guilhem'
from Player import *
from Tools import *
import random
import Time
import World
import time


class Enemy:
    def __init__(self, tag, hp, attack, defense, drop):
        self.tag = tag
        self.HP = hp
        self.attack = attack
        self.defense = defense
        self.drop = drop

class Fight:
    def __init__(self):
        self.Combat_Mode = 0
        self.enemy = None
        self.tour = 1

    def fight(self, joueur,enemy2):
        time.sleep(1)
        writeinfper('COMBAT')
        self.Combat_Mode = 1
        self.enemy = enemy2
        self.fight_global(joueur)


    def fight_global(self,joueur):
        if self.enemy.HP <= 0:
            write('>>>>>>',self.enemy.tag[:-1], 'is defeated !<<<<<<')
            position = World.map[tuple(joueur.location)]
            del position.monstersin[self.enemy.tag[:-1]+' '+self.enemy.tag[-1]]
            if enemy_count(tuple(joueur.location))[1] != 0:
                weak = enemy_count(tuple(joueur.location))[1]-1
                write('A', str(World.map[tuple(joueur.location)].monstersin['Weak '+str(weak)].tag)[:-1],'runs furiously towards you')
                self.fight(joueur, World.map[tuple(joueur.location)].monstersin['Weak '+str(weak)])
                return
            else:
                self.enemy = None
                writeinfper(World.map[tuple(joueur.location)].name)
                self.tour = 1
                self.Combat_Mode = 0

        if self.tour % 2 == 1:
            pass
        else:
            self.enemy_fight(joueur, self.enemy)

        # self.fight_global(joueur, enemy)


    def enemy_fight(self,joueur, enemy):
        if joueur.defenseeqpd == '':
            defensevalue = 1
        else:
            defensevalue = joueur.defenseeqpd.defense
        damage = int((self.enemy.attack - defensevalue)*(1.2+random.randint(-5, 5)/10))
        if damage < 0:
            damage = 0
        joueur.HP -= damage
        write(self.enemy.tag[:-1], 'hit you.', joueur.HP, damage)
        self.tour += 1

    def attack(self, joueur):
        if joueur.attackeqpd == '':
                weapon = 'your hands'
                weaponvalue = 1
        else:
            weapon = joueur.attackeqpd.tag
            weaponvalue = joueur.attackeqpd.attack
        damage = int((weaponvalue - self.enemy.defense)*(1-(4-Time.hungry)/5)*(1.2+random.randint(-5, 5)/10))
        if damage < 0:
            damage = 0
        self.enemy.HP -= damage
        write('You hit', self.enemy.tag[:-1], 'with', weapon, '.')
        self.tour += 1