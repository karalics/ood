#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Es handelt sich hier um Python2 Code. Dieses File

"""Ein Python Decorator ist eine  Funktion (oder auch ein Objekt, 
dass eine __call__ method besitzt), die als Parameter ebenfalls 
eine  Funktion entgegennimmt und eine Funktion zurückgibt. 

Ein Dekorator nimmt eine Funktion, macht etwas mit dieser Funktion. 
Praktische Anwendung ist zum Beispiel Code Injection. Bsp Beim Django
Web Framework: mit @login_required kann man einer View Funktion einfach
angeben, dass ein Login erforderlich ist um entsprechende INhalte sehen
zu können. """

#Einfaches Beispiel

def dekorfunk(func):
	func.__doc__ += ' - DEKORATION!'
	return func

@dekorfunk
def myprint():
	""" Das ist ein DocString"""
	pass

print myprint.__doc__
#LOG: Das ist ein DocString - DEKORATION!

"""Die Dekoration erfolgt exakt nach dem erstellen der myprint
Funktion."""

#Andere Schreibweise beim Anwenden eines Decorators:
myprint2 = dekorfunk(myprint)
print myprint2.__doc__

"""An dieser Stelle wird die bereits dekorierte myprint funktion
nochmals dekoriert"""

#Log(zweiter print): Das ist ein DocString - DEKORATION! - DEKORATION!


""" Bei dieser Schreibweise kann man noch gut sehen wie die verschachtelten
Docorators functionieren, bzw in welcher Reihenfolge."""

def dekorfunk2(func):
	func.__doc__ += ' - Ich bin die Umliegende Dekoration'
	return func
	

def myprint():
	""" Das ist ein DocString"""
	pass	
myprint3 = dekorfunk2(dekorfunk(myprint))
print myprint3.__doc__
#Log  Das ist ein DocString - DEKORATION! - Ich bin die Umliegende Dekoration

#entsprechend genau gleich in anderer schreibweise

@dekorfunk2
@dekorfunk
def myprint():
	""" Das ist ein DocString"""
	pass

print myprint.__doc__
#Log  Das ist ein DocString - DEKORATION! - Ich bin die Umliegende Dekoration


"""Und noch ein Beispiel mit einer 
komplett verändertetn Funktion als Rückgabewert"""

def istinteger(func):
	def inner(*args):
		for arg in list(args):
			if not isinstance(arg, int):
				raise TypeError('%s akzeptiert nur Integer als Parameter.' 
				% func.__name__)
				
		return func(*args)
	return inner

@istinteger
def summe(a, b):
	return a+b

print summe(25, 33)
#Log: 58

print summe('a', 33)
#Log: TypeError: summe akzeptiert nur Integer als Paramter.
