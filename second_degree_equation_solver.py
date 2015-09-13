# -*- coding: utf-8 -*-
import sys
import math

print " _____             _   _            _____     _                      ___   "
print "|   __|___ _ _ ___| |_|_|___ ___   |   __|___| |_ _ ___ ___    _ _  |_  |  "
print "|   __| . | | | .'|  _| | . |   |  |__   | . | | | | -_|  _|  | | |_ _| |_ "
print "|_____|_  |___|__,|_| |_|___|_|_|  |_____|___|_|\_/|___|_|     \_/|_|_____|"
print "        |_|                                                                "

print "\nWelcome in the Equation Resolver. Please give the values for 'a', 'b' and 'c' as follows: ax^2+bx+c = 0.\n"

a = float(input("Value of 'A': "))

if a != 0:
	print "A = %s" % (a)
else:
	sys.exit("Invalid value. Please enter only numbers other than zero.")

b = float(input("Value of 'B': "))

if b != 0:
	print "B = %s" % (b)
else:
	sys.exit("Invalid value. Please enter only numbers other than zero.")

c = float(input("Value of 'C': "))

if c != 0:
	print "C = %s" % (c)
else:
	sys.exit("Invalid value. Please enter only numbers other than zero.")

discriminant = (b * b) - 4 * (a * c)

if discriminant >= 0:
	print "\nThe discriminant is equal to: %s.\n" % (discriminant)
else:
	sys.exit("The equation is unresolvable. The discriminant is negative.")

x1 = (-b - math.sqrt(discriminant) ) / (2 * a)
x2 = (-b + math.sqrt(discriminant) ) / (2 * a)
x3 = (-b) / (2 * a)

if discriminant == 0:
    print "Sole solution of the equation: %s" % (x3)
else:
	print "Solutions: (%s; %s) \n\nThank you for using the Equation Solver !" % (x1, x2)
