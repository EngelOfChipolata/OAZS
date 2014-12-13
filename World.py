__author__ = 'guilhem'
import random
import Fight
dict_item = {}
map = {}



class Location():
    def __init__(self, position, name, tag, description, itemsin, monstersin):
        self.position = position
        self.name = name    #Nom de l'endroit
        self.tag = tag
        self.description = description       #Description de l'endroit
        self.items = itemsin     #Items contenus dans l'endroit
        self.monstersin = {} #Nombres de Monstres contenus dans l'endroit


class Item():
    def __init__(self, name, tag, description, gainHP, gainhungry, gainthirsty, attack, defense, weight):
        self.name = name        #Nom de l'item (Output+Input)
        self.tag = tag          #Tag de l'item (Input)
        self.description = description      #Description de l'item
        self.gainHP = gainHP   #Nombre de HP gagné en mangeant l'item
        self.gainhungry = gainhungry #Nombre de points de faim gagné en mangeant l'item
        self.gainthirsty = gainthirsty #Nombre de points de soif gagné en mangeant l'item
        self.attack = attack  #Valeur en attaque de l'objet si équipé (-1 = non équipable en arme)
        self.defense = defense #Valeur en défense de l'objet si équipé (-1 = non équipable en armure)
        self.weight = weight #Poids de l'item


def load_items(filename):
    file = open(filename) #ouverture du fichier
    print('Loading Items...', end='')
    global dict_item #Création du dictionnaire des items
    for line in file:  #Parcours du fichier ligne par ligne
        blocs = line[0:].split('_')  #Séparation en liste des blocs séparés par des '_'
        if blocs[0]!='\n' and '#' not in blocs:  #Saut des commentaires et des sauts de lignes dans la lecture du fichier
            dict_item[str(blocs[1])] = Item(blocs[0], blocs[1], blocs[2], int(blocs[3]), int(blocs[4]), int(blocs[5]), int(blocs[6]), int(blocs[7]), float(blocs[8])) #Ajout de l'item au dictionnaire
    print('Done')
    # for i in dict_item:    #Affichage des items chargés (A SUPPPRIMER)
    #     print(i, '==', dict_item[i].description)


def load_world(filename):
    global map #Création du dictionnaire des lieux
    map = {(0,0):Location((0,0),'Cabin', 'cabin', 'The small cabin you woke in.',[],[])}
    file = open(filename) #ouverture du fichier
    print('Loading Map...', end='')
    for line in file:  #Parcours du fichier ligne par ligne
        blocs = line[0:].split('_')  #Séparation en liste des blocs séparés par des '_'
        if blocs[0]!='\n' and '#' not in blocs:  #Saut des commentaires et des sauts de lignes dans la lecture du fichier
            loca = (0,0)
            while loca in map:
                loca = (random.randint(-2, 2), random.randint(-2, 2))
            map[loca] = Location(loca, blocs[0], blocs[1], blocs[2], blocs[3], blocs[4])  #Ajout du lieu au dictionnaire
    for i in range(-2, 3, 1):
        for j in range(-2, 3, 1):
            if (i, j) not in map:
                map[(i, j)] = Location((i, j), 'Desert', 'desert', 'Sand... Everywhere.', [], [])
    ('Done.')
    print('Mapping enemies...')
    enemy_mapping(1)
    print('Done.')
    # for i in map:    #Affichage des lieu chargés (A SUPPPRIMER)
    #      print(i, '==', map[i].description, map[i].name )


def enemy_mapping(day):
    global map
    for u in map:
        (i, j) = u
        if (i, j) != (0, 0):
            weak = random.randint(0, day) + random.randint(0, int((abs(i)+abs(j))/2))
            common = random.randint(0, abs(day-3)) + random.randint(0, int((abs(i)+abs(j))/2))
            heavy = random.randint(0, abs(day-5)) + random.randint(0, int((abs(i)+abs(j))/2))
            if weak != 0:
                for k in range(weak):
                    map[(i, j)].monstersin['Weak '+str(k)] = Fight.Enemy('Weak'+str(k), random.randint(10, 15), random.randint(1, 5), 0, [])
            if day >= 2 and common != 0:
                for k in range(common):
                    map[(i, j)].monstersin['Common '+str(k)] = Fight.Enemy('Common'+str(k), random.randint(20, 25), random.randint(4, 10), 0, [])
            if day >= 4 and heavy !=0:
                for k in range(heavy):
                    map[(i, j)].monstersin['Heavy '+str(k)] = Fight.Enemy('Heavy'+str(k), random.randint(30, 40), random.randint(12, 20), 1, [])
        # print(u,map[u].monstersin)




