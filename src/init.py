#! /usr/bin/env python
# -*- coding: utf-8 -*-	

global afterinit
c.delete("all")	#methode qui nettoie c
global mot
mot = non_consecutif()
global taille
taille = len(mot)
global trou
trou = '-'
global devine
devine = trou * taille
global P
# la pendaison... une liste de dessins
P = [	'c.create_line(40, 185, 140, 185, width=20, fill="maroon")',
	'c.create_line(70, 185, 70, 10, width=7, fill="maroon")',
	'c.create_line(66, 10, 129, 10, width=7, fill="maroon")',
	'c.create_line(127, 13, 127, 60, width=4, fill="yellow")',
	'c.create_oval(110, 30, 129, 49, width=1, fill="black")',
	'c.create_rectangle(116, 50, 136, 100, fill="black")',
	'c.create_line(120, 50, 100, 100, width=4, fill="black")',
	'c.create_line(136, 50, 146, 100, width=4, fill="black")',
	'c.create_line(120, 100, 120, 150, width=7, fill="black")',
	'c.create_line(133, 100, 133, 150, width=7, fill="black")' ]

global keyHistory
keyHistory = []	#nouvelle liste pour contenir l'historique des touches enfoncées
if afterinit : affiche()
afterinit = True

