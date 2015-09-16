# -*- coding: utf-8 -*-
#Import libraries
from sys import exit
from math import sqrt
#Print title
print "   ____               __  _             ____     __               _   __  ___ "
print "  / __/__ ___ _____ _/ /_(_)__  ___    / __/__  / /  _____ ____  | | / / |_  |"
print " / _// _ `/ // / _ `/ __/ / _ \/ _ \  _\ \/ _ \/ / |/ / -_) __/  | |/ / / __/ "
print "/___/\_, /\_,_/\_,_/\__/_/\___/_//_/ /___/\___/_/|___/\__/_/     |___(_)____/ "
print "      /_/                                                                     "
#Welcome phrase
print "\nWelcome in the Equation Solver 2.0 by V3sth4cks153. Please give the values for 'a', 'b' and 'c' as follows: ax^2+bx+c = 0.\n"
#Define check function
def check(x):
    if x != 0:
	    pass
    else:
	    exit("Invalid value. Please enter only numbers other than zero.")
#Input and check
a = float(input("Value of 'A': "))
check(a)
b = float(input("Value of 'B': "))
check(b)
c = float(input("Value of 'C': "))
check(c)
#Formulas
dis = (b * b) - 4 * (a * c)
x1 = (-b - sqrt(dis) ) / (2 * a)
x2 = (-b + sqrt(dis) ) / (2 * a)
x3 = (-b) / (2 * a)
#Calculus conditions
if dis >= 0:
	print "\nThe discriminant is equal to: %s.\n" % (dis)
else:
	exit("The equation has no real roots: The discriminant is negative.")

if dis == 0:
    print "Sole root of the equation: (%s)" % (x3)
else:
	print "Roots: (%s; %s) \n\nThank you for using the Equation Solver by V3sth4cks153 !" % (x1, x2)
