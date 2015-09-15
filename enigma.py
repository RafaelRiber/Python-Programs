# -*- coding: utf-8 -*-
import sys
import time
from os import system
from os import name

def cls():
	system(['clear','cls'][name == 'nt'])

def go(ans):
	if ans == "oui" or ans == "o":
		print "Alors c'est parti !"
	elif ans == "non" or ans == "n":
		sys.exit("Pas de problème ! Revenez quand vous voulez !")
	else:
		sys.exit("Pas de problème ! Revenez quand vous voulez !")

def ans_a(ans):
	if ans == "A" or ans == "a":
		print "Bonne réponse !"
	elif ans == "B" or ans == "b":
		exit("Mauvaise réponse ! Dommage !")
	else:
		exit("Réponse invalide.")

def ans_b(ans):
	if ans == "B" or ans == "b":
		print "Bonne réponse !"
	elif ans == "A" or ans == "a":
		exit("Mauvaise réponse ! Dommage !")
	else:
		exit("Mauvaise réponse ! Dommage !")

print "╔═╗╔╗╔╦╔═╗╔╦╗╔═╗    "
print "║╣ ║║║║║ ╦║║║╠═╣    "
print "╚═╝╝╚╝╩╚═╝╩ ╩╩ ╩    "

print "Bienvenue dans Enigma."

age = raw_input("Quel est votre âge ? ")

if age >= 12:
	print "Vous avez l'âge de jouer"
else:
	sys.exit("Vous êtes trop jeune pour jouer. Désolé !")

nom = raw_input("Quel est votre nom ? ")

if nom.isalpha and len(nom) > 0:
	print "Bonjour %s." % (nom)
else:
	sys.exit("Je ne crois pas que cela soit votre nom... Merci de relancer le programme.")

rawans = raw_input("Alors %s, prêt à jouer ? Répondre par 'oui' ou par 'non': " % (nom) )

cls()

ans = rawans.lower()
go(ans)

print "\nVoici le principe du jeu: vous allez être présenté avec plusieurs énigmes et questions. \nPour chacune, vous aurez deux réponses a choix. Toute réponse correcte vous donnera 5 points,\ntoute réponse fausse vous enlèvera un point."

rawans = raw_input("\nDébuter le jeu ? Répondre par 'oui' ou par 'non': ")

ans = rawans.lower()

cls()
go(ans)
#----------------------------------------------------------------------------
print "\nPremière question:"
print "David a 10 ans, son petit frère Franck a la moitié de son âge.\nQuand David sera 10 fois plus âgé, quel âge aura Franck ?"
print "A: 95 ans"
print "B: 50 ans"

ans = raw_input("\nQuelle est la bonne réponse ? Répondre 'A' ou 'B': ")

cls()
ans_a(ans)
#----------------------------------------------------------------------------
print "\nBien joué %s ! Allons la question suivante." % (nom)

print "\nDeuxième question:"
print "Si nous ne sommes pas le lendemain de lundi ou le jour avant jeudi, que demain n'est pas dimanche,\nque ce n'était pas dimanche hier et que le jour d'après-demain n'est pas samedi,\net que le jour avant hier n'était pas mercredi, quel jour sommes-nous ?"
print "A: Jeudi"
print "B: Dimanche"

ans = raw_input("\nQuelle est la bonne réponse ? Répondre 'A' ou 'B': ")

cls()
ans_b(ans)
#----------------------------------------------------------------------------
print "\nBien joué %s ! Allons la question suivante." % (nom)

print "\nTroisième question:"
print "Quel nombre divisé par lui-même donne son double ?"
print "A: 0.5"
print "B: 2.5"

ans = raw_input("\nQuelle est la bonne réponse ? Répondre 'A' ou 'B': ")

cls()
ans_a(ans)
#----------------------------------------------------------------------------
print "\nBien joué %s ! Allons la question suivante." % (nom)

print "\nQuatrième question:"
print "Sur un arbre à 2 branches, des oiseaux se parlent, l'un d'en haut dit à ceux d'en bas 'Si un de vous nous rejoint, nous serons alors 2 fois plus que vous,\npar contre si un de nous descend, nous serons alors à égalité'. Combien y a-t-il d'oiseaux sur les branches ?"
print "A: 7 en haut et 5 en bas"
print "B: 5 en haut et 2 en bas"

ans = raw_input("\nQuelle est la bonne réponse ? Répondre 'A' ou 'B': ")

cls()
ans_a(ans)

cls()
print "Vous êtes arrivés au bout du jeu! Félicitations !
