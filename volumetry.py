# -*- coding: utf-8 -*-
from os import system
from os import name
#http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Volumetry%20v1
print "____   ____    .__                        __                         ____ "
print "\   \ /   /___ |  |  __ __  _____   _____/  |________ ___.__. ___  _/_   |"
print " \   Y   /  _ \|  | |  |  \/     \_/ __ \   __\_  __ <   |  | \  \/ /|   |"
print "  \     (  <_> )  |_|  |  /  Y Y  \  ___/|  |  |  | \/\___  |  \   / |   |"
print "   \___/ \____/|____/____/|__|_|  /\___  >__|  |__|   / ____|   \_/  |___|"
print "                                \/     \/             \/                  "
def cls():
	system(['clear','cls'][name == 'nt'])

choice = str(raw_input("\n\nWelcome in the volumetry calculator ! What would you like to calculate ?\n\nA: Molarity of substance A\nB: Volume of substance A\nC: Molarity of substance B\nD: Volume of substance B\n\nYour answer: ")).lower()

if choice == "a":
    cls()
    print "You chose to calculate the molarity of substance A.\n"
    vola = float(input("What volume of substance A do you have (in liters) ? "))
    volb = float(input("What volume of substance B do you have (in liters) ? "))
    molb = float(input("What is the molarity of substance B ? "))
    coefa = float(input("What is the stoichiometric coefficient of substance A ? "))
    coefb = float(input("What is the stoichiometric coefficient of substance B ? "))
    mola = (molb * volb * coefa) / (coefb *vola)

    print "\nThe molarity of substance A is: %s [M].\n\nThank you for using the volumetry calculator !\n" % (mola)

elif choice == "b":
    cls()
    print "You chose to calculate the volume of substance A.\n"
    mola = float(input("What is the molarity of substance A ? "))
    molb = float(input("What is the molarity of substance B ? "))
    volb = float(input("What volume of substance B do you have (in liters) ? "))
    coefa = float(input("What is the stoichiometric coefficient of substance A ? "))
    coefb = float(input("What is the stoichiometric coefficient of substance B ? "))
    vola = (molb * volb * coefa) / (coefb * mola)

    print "\nThe volume of substance A is: %s [l].\n\nThank you for using the volumetry calculator !\n" % (vola)

elif choice == "c":
    cls()
    print "You chose to calculate the molarity of substance B.\n"
    vola = float(input("What volume of substance A do you have (in liters) ? "))
    volb = float(input("What volume of substance B do you have (in liters) ? "))
    mola = float(input("What is the molarity of substance A ? "))
    coefa = float(input("What is the stoichiometric coefficient of substance A ? "))
    coefb = float(input("What is the stoichiometric coefficient of substance B ? "))
    molb = (mola * vola * coefb) / (coefa * volb)

    print "\nThe molarity of substance B is: %s [M].\n\nThank you for using the volumetry calculator !\n" % (molb)

elif choice == "d":
    cls()
    print "You chose to calculate the volume of substance B.\n"
    mola = float(input("What is the molarity of substance A ? "))
    molb = float(input("What is the molarity of substance B ? "))
    vola = float(input("What volume of substance A do you have (in liters) ? "))
    coefa = float(input("What is the stoichiometric coefficient of substance A ? "))
    coefb = float(input("What is the stoichiometric coefficient of substance B ? "))
    volb = (mola * vola * coefb) / (coefa * molb)

    print "\nThe volume of substance B is: %s [l].\n\nThank you for using the volumetry calculator !\n" % (volb)
