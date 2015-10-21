# -*- coding: utf-8 -*-
#Import libraries
from sys import exit
#Define check function
def check(x):
    if type(x) == int and x >= 0:
        pass
    elif type(x) == float or type(x) == str:
        exit("Invalid value. Please enter a valid number. (no decimals and only numeral)")
    else:
        exit("Invalid value. Please enter a valid number.")
#Input and check
ten_francs = input("1/13 - How many ten francs bills do you have ? ")
check(ten_francs)

twenty_francs = input("2/13 - How many twenty francs bills do you have ? ")
check(twenty_francs)

fifty_francs = input("3/13 - How many fifty francs bills do you have ? ")
check(fifty_francs)

hundred_francs = input("4/13 - How many hundred francs bills do you have ? ")
check(hundred_francs)

two_hundred_francs = input("5/13 - How many two hundred francs bills do you have ? ")
check(two_hundred_francs)

thousand_francs = input("6/13 - How many thousand francs bills do you have ? ")
check(thousand_francs)

five_francs = input("7/13 - How many five francs coins do you have ? ")
check (five_francs)

two_francs = input("8/13 - How many two francs coins do you have ? ")
check(two_francs)

one_franc = input("9/13 - How many one franc coins do you have ? ")
check(one_franc)

fifty_cents = input("10/13 - How many fifty cents coins do you have ? ")
check(fifty_cents)

twenty_cents = input("11/13 - How many twenty cents coins do you have ? ")
check(twenty_cents)

ten_cents = input("12/13 - How many ten cents coins do you have ? ")
check(ten_cents)

five_cents = input("13/13 - How many five cent coins do you have ? ")
check(five_cents)

#Count total
total = (ten_francs * 10) + (twenty_francs * 20) + (five_francs * 5) + (hundred_francs * 100) + (two_hundred_francs * 200) + (thousand_francs * 1000) + (five_francs * 5) + (two_francs * 2) + (one_franc * 1) + (fifty_cents * 0.5) + (twenty_cents * 0.2) + (ten_cents * 0.1) + (five_cents * 0.05)

print "You have exactly %s francs." % (total)
