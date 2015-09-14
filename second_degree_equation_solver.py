# -*- coding: utf-8 -*-
from sys import exit
from math import sqrt

print " _____             _   _            _____     _                      ___   "
print "|   __|___ _ _ ___| |_|_|___ ___   |   __|___| |_ _ ___ ___    _ _  |_  |  "
print "|   __| . | | | .'|  _| | . |   |  |__   | . | | | | -_|  _|  | | |_ _| |_ "
print "|_____|_  |___|__,|_| |_|___|_|_|  |_____|___|_|\_/|___|_|     \_/|_|_____|"
print "        |_|                                                                "

print "\nWelcome in the Equation Resolver by V3sth4cks153. Please give the values for 'a', 'b' and 'c' as follows: ax^2+bx+c = 0.\n"

a = float(input("Value of 'A': "))

if a != 0:
	print "A = %s" % (a)
else:
	exit("Invalid value. Please enter only numbers other than zero.")

b = float(input("Value of 'B': "))

if b != 0:
	print "B = %s" % (b)
else:
	exit("Invalid value. Please enter only numbers other than zero.")

c = float(input("Value of 'C': "))

if c != 0:
	print "C = %s" % (c)
else:
	exit("Invalid value. Please enter only numbers other than zero.")

discriminant = (b * b) - 4 * (a * c)

if discriminant >= 0:
	print "\nThe discriminant is equal to: %s.\n" % (discriminant)
else:
	exit("The equation is unsolvable: The discriminant is negative.")

x1 = (-b - sqrt(discriminant) ) / (2 * a)
x2 = (-b + sqrt(discriminant) ) / (2 * a)
x3 = (-b) / (2 * a)

if discriminant == 0:
    print "Sole solution of the equation: %s" % (x3)
else:
	print "Solutions: (%s; %s) \n\nThank you for using the Equation Solver by V3sth4cks153 !" % (x1, x2)
