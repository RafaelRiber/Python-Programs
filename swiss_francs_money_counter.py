# -*- coding: utf-8 -*-
ten_francs = float(input("How many ten francs bills do you have ? "))
twenty_francs = float(input("How many twenty francs bills do you have ? "))
fifty_francs = float(input("How many fifty francs bills do you have ? "))
hundred_francs = float(input("How many hundred francs bills do you have ? "))
two_hundred_francs = float(input("How many two hundred francs bills do you have ? "))
thousand_francs = float(input("How many thousand francs bills do you have ? "))
five_francs = float(input("How many five francs coins do you have ? "))
two_francs = float(input("How many two francs coins do you have ? "))
one_franc = float(input("How many one franc coins do you have ? "))
fifty_cents = float(input("How many fifty cents coins do you have ? "))
twenty_cents = float(input("How many twenty cents coins do you have ? "))
ten_cents = float(input("How many ten cents coins do you have ? "))
five_cents = float(input("How many five cent coins do you have ? "))

total = (ten_francs * 10) + (twenty_francs * 20) + (five_francs * 50) + (hundred_francs * 100) + (two_hundred_francs * 200) + (thousand_francs * 1000) + (five_francs * 5) + (two_francs * 2) + (one_franc * 1) + (fifty_cents * 0.5) + (twenty_cents * 0.2) + (ten_cents * 0.1) + (five_cents * 0.05)

print "You have exactly %s francs." % (total)
