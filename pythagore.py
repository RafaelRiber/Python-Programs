# -*- coding: utf-8 -*-
#Import de libraries
from math import sqrt
from sys import exit
#Bienvenue
know = str(raw_input("Bienvenue dans le solveur du Théorème de Pythagore. \nQue connaissez-vous dans le triangle ? \n\nA: 1 cathète + hypoténuse\nB: Deux cathètes\n\nRéponse: "))
#Choix puis calculs
if know == "A" or know == "a":
    a = float(input("\nLongueur de l'hypoténuse: "))
    b = float(input("Longueur du cathète: "))

    if a > 0 and b > 0:
        c = sqrt(a**2 - b**2)
        print "\nLe deuxième cathète à une longueur de %s" % (c)
    else:
        exit("\nCalcul impossible.")
elif know == "B" or know == "b":
    b = float(input("Longueur du premier cathète: "))
    c = float(input("Longueur du deuxième cathète: "))

    if b > 0 and c > 0:
        a = sqrt(b**2 + c**2)
        print "\nL'hypoténuse a une longueur de %s" % (a)
    else:
        exit("\nCalcul impossible.")
else:
    exit("Réponse non valide.")
