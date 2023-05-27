"""
Todo list:
Add the stronger spells to the build script
Decide on how to do enemies
Fix circle of blessings.
Make haste a touch spell.
"""

import os
import scipy.misc
from scipy import ndimage
from PIL import Image
import random
import csv

"""
f = open("spells.txt")
lines = f.read()
splitlines = lines.split("\n")
print(len(splitlines))
splitlines = splitlines[1:len(splitlines)-1]
print(len(splitlines))
spells = splitlines
"""


cardCount = 0
"""Name\tRules Text\tMana Cost\tClass Type\tSubtype\tAttack\tHealth\tFlavourtext"""
units = ["""Pengin\t\t3\tSpell\tPengin\t3\t1\t"Wak Wak" -Pengin"""]

#Cards
with open('db.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if(os.path.exists("icons\\"+row['Name']+".png")):
        if(len(row['Name'])<15):
          with open("unit.svg") as cards:
            cardTemplate = cards.read()
        else:
          with open("unit_small.svg") as cards:
            cardTemplate = cards.read()
        mod = cardTemplate.replace("NAME",row['Name']).replace("RULESTEXT",row['Rules Text']).replace("MANA",row['Mana Cost']).replace("TYPE",row['Type'] + " - " + row['Subtype']).replace("icon.png","icons\\"+row['Name']+".png").replace("FLAVOURTEXT",row['Flavourtext'])
        if(row['Type']=="Unit"):
          mod=mod.replace("ATTACK",row['Attack']).replace("HEALTH",row['Health'])
        elif(row['Type']=="Building"):
          mod=mod.replace("unit.png","building.png").replace("ATTACK","").replace("HEALTH",row['Health'])
        elif(row['Type']=="Spell"):
          mod=mod.replace("unit.png","spell.png").replace("ATTACK","").replace("HEALTH","")
        f = open("temp\\"+row['Name']+".svg", "w")
        f.write(mod)
        f.close()
        os.system("inkscape.com -w 825 -h 1125 -e \"cardlist\\"+row['Name']+".png\"" + " \".\\temp\\"+row['Name']+".svg\"")
      else:
        os.system("copy icons\\_default.png \"icons\\"+row['Name']+".png\"")
