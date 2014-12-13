__author__ = 'guilhem'
import World


class Player():
    def __init__(self):
        self.location = [0, 0] #Position passées et actuelle du joueur (x,y)
        self.inventory = [] #Inventaire du joueur
        self.HP = 100         #Points de vie du joueur
        self.attackeqpd = ''    #Arme équipée
        self.defenseeqpd = ''   #Défense équipée
        self.thirst = 100         #Soif
        self.hungry = 100         #Faim
