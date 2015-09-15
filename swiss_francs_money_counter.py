# -*- coding: utf-8 -*-
from sys import exit

def check(x):
    if type(x) == int and x >= 0:
        print "%s is a valid number. Go on." % (x)
    elif type(x) == float or type(x) == str:
        exit("Invalid value. Please enter a valid number.")
    else:
        exit("Invalid value. Please enter a valid number.")

ten_francs = input("How many ten francs bills do you have ? ")
check(ten_francs)

twenty_francs = input("How many twenty francs bills do you have ? ")
check(twenty_francs)

fifty_francs = input("How many fifty francs bills do you have ? ")
check(fifty_francs)

hundred_francs = input("How many hundred francs bills do you have ? ")
check(hundred_francs)

two_hundred_francs = input("How many two hundred francs bills do you have ? ")
check(two_hundred_francs)

thousand_francs = input("How many thousand francs bills do you have ? ")
check(thousand_francs)

five_francs = input("How many five francs coins do you have ? ")
check (five_francs)

two_francs = input("How many two francs coins do you have ? ")
check(two_francs)

one_franc = input("How many one franc coins do you have ? ")
check(one_franc)

fifty_cents = input("How many fifty cents coins do you have ? ")
check(fifty_cents)

twenty_cents = input("How many twenty cents coins do you have ? ")
check(twenty_cents)

ten_cents = input("How many ten cents coins do you have ? ")
check(ten_cents)

five_cents = input("How many five cent coins do you have ? ")
check(five_cents)

total = (ten_francs * 10) + (twenty_francs * 20) + (five_francs * 50) + (hundred_francs * 100) + (two_hundred_francs * 200) + (thousand_francs * 1000) + (five_francs * 5) + (two_francs * 2) + (one_franc * 1) + (fifty_cents * 0.5) + (twenty_cents * 0.2) + (ten_cents * 0.1) + (five_cents * 0.05)

print "You have exactly %s francs." % (total)
