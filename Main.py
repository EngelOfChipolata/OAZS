__author__ = 'guilhem'
import Message
import World
from Player import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Ui
import sys
import Saisie
import _thread
import Tools
import Time
import Fight


World.load_items('Ressources/Item_list') #Chargement de la liste d'items
World.load_world('Ressources/World_list') #Chargement de la liste des lieux
joueur = Player() #Création du joueur
root = QApplication(sys.argv)
widg = QWidget()
widg.arrowdown = QShortcut(QKeySequence("Down"), widg)
widg.arrowup = QShortcut(QKeySequence("Up"), widg)
UI = Ui.Ui_Ui()
UI.setupUi(widg)
widg.show()
Tools.Gset(UI)
FightingClass = Fight.Fight()
UI.playerinput.returnPressed.connect(lambda: Saisie.saisie(joueur, UI, FightingClass))
widg.arrowdown.activated.connect(lambda: Saisie.call(-1))
widg.arrowup.activated.connect(lambda: Saisie.call(1))
joueur.inventory.append(World.dict_item['banana'])
joueur.inventory.append(World.dict_item['sword'])
joueur.inventory.append(World.dict_item['clothes'])
Time.def_joueur(joueur)
Tools.write('What a party... Your head is heavy, the morning light is kicking your ass. You stand up and try to open your eyes. But... Wait, you aren\'t at your home ! You just wake up in a small cabin in the middle of the desert...Yeah, what a party...')
Time.OFFSET = 0
_thread.start_new_thread(Time.igtime, ())
root.exec_()