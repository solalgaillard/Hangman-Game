#! /usr/bin/env python
# -*- coding: utf-8 -*-	


from Tkinter import *
from random import choice
from os import chdir	#permet d'accéder au dossier où sont contenus les fichier externes
chdir('src')
import sys

if len(sys.argv) == 2 and (sys.argv[1] == 'facile' or sys.argv[1] == 'intermediaire' or sys.argv[1] == 'difficile' or sys.argv[1] == 'english') :

	def get_list(fichier) :
		flux = open(fichier, 'r')
		listeMots = flux.read().decode('utf-8').lower().split()
		flux.close()
		return listeMots
	
	def put_list(fichier, mot) :
		flux = open(fichier, 'w')
		flux.write(mot.encode('utf-8'))
		flux.close()
		
	def non_consecutif() :
		mot = choice(mots)
		if get_list('dernier mot')[0] == mot : return non_consecutif()
		else : 
			put_list('dernier mot', mot)
			return mot

	mots = get_list(sys.argv[1])

	def actualise(event) :
		global devine
		global keyHistory	#utilise la variable globale keyHistory
		if P and trou in devine :
			currentKey = event.char.decode('utf-8').lower()	#charge dans la variable currentKey la touche enfoncée en unicode et miniscule
			nouveau = valide(currentKey, mot, devine, taille)
			if devine != nouveau : devine = nouveau
			elif event.char != '' and currentKey not in keyHistory : eval(P.pop(0))	#permettre modifier-keys pour clavier non-standard et valide seulement si le caractère n'a pas été appelé précedemment
			if currentKey not in keyHistory : keyHistory += currentKey	#ajoute seulement si le caractère n'est pas déjà dans la liste
			affiche()

	def valide(C, original, devine, taille, R = '') :
		for x in range(taille) :
			if original [x] == C : R += original [x]
			else : R += devine [x]
		return R

	def affiche() :
		L = len(P)
		LT.configure(text = devine)
		LP.configure(text = str(L))
		if not L : LM ['text'] = mot
		else : LM ['text'] = '' #ajouté pour réinitialisation
	
	
	def start() :
		execfile("init.py")	#utilise execfile pour suivre les consignes mais pas nécessaire
	

	top = Tk()
	top.title("devine le mot")
	top.bind("<Key>", actualise)
	c = Canvas(top, bg='light grey', height=200, width=200)
	c.pack(side = LEFT)	
	afterinit = False	#switch pour que la première initialisation se passe bien. Que la fonction affiche ne se déclenche pas car elle modifie des objets pas encore initialisés
	start()		#fonction d'initialisation et handler pour callback 'Button'
	Button(top, text='start', command=start).pack(side=TOP)
	Button(top, text='stop', command=top.quit).pack(side=TOP)
	LT = Label(top, text=devine, fg='red') ; LT.pack()
	LM = Label(top, text='', fg='red') ; LM.pack()
	LP = Label(top, text=str(len(P)), fg='blue') ; LP.pack()	
	top.mainloop()

else : print "Veuillez choisir la liste des mots parmis les fichiers facile, intermediaire, difficile"

