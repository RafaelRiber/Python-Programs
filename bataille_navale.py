# -*- coding: utf-8 -*-
from random import randint
from os import system
from os import name

def cls():
	system(['clear','cls'][name == 'nt'])

plateau = []

for x in range(0, 5):
    plateau.append(["O"] * 5)

def afficher_plateau(plateau):
    for ligne in plateau:
        print " ".join(ligne)

afficher_plateau(plateau)

def alea_ligne(plateau):
    return randint(0, len(plateau) - 1)

def alea_col(plateau):
    return randint(0, len(plateau[0]) - 1)

bateau_x = alea_ligne(plateau)
bateau_y = alea_col(plateau)

for tour in range(11):
    tir_x = int(raw_input("Quelle ligne ? "))
    tir_y = int(raw_input("Quelle colonne ? "))

    if tir_x == bateau_x and tir_y == bateau_y:
        print "Bravo ! Vous avez eu mon bateau !"
        break
    else:
        if (tir_x < 0 or tir_x > 4) or (tir_y < 0 or tir_y > 4):
            print "Oups ! Vous devez viser l'océan."
        elif(plateau[tir_x ][tir_y ] == "X"):
            print "Cette case est déjà découverte."
        else:
            print "\nDommage ! Vous avez raté mon bateau !"
            plateau[tir_x ][tir_y ] = "X"

    print "\nEssai no: " + str(tour + 1) +"/10" + "\n"
    afficher_plateau(plateau)

if tour == 10:
    cls()
    print "Game Over !"
    print "Les coordonées du bateau étaient: (%s, %s)" % (bateau_x, bateau_y)
