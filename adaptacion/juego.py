#!/usr/bin/python
import getch
from number import Number
import math
from puntuacion import Score
class Juego:
    def __init__(self):
        self.jugando = False
	self.time = 200


def main():
    print "Bienvenido al juego"
    print("Quieres crear tu propia partida?(y/n)")
    propia = getch.getch()
    if(propia == "y"):
	minNumber = input("Introduce el numero minimo: ")
	maxNumber = input("Introduce el mumero maximo: ")
    else:
	minNumber = 0
	maxNumber = 100
    numero=Number(minNumber, maxNumber).number
    intentos = Score(minNumber, maxNumber).intentos
    print "Intente adivinar el numero entre " + str(minNumber) + " y " + str(maxNumber)
    print "Tienes",intentos,"intentos"


main()
