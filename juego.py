#!/usr/bin/python
import random
import math
import re

#Class getch - Gets a single character from standard input.  Does not echo to the screen(Unix and Windows)
class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
    def __call__(self): return self.impl()
class _GetchUnix:
    def __init__(self):
        import tty, sys
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
getch = _Getch()


#Game Start
print "Bienvenido al juego"
salir = False
misPuntos = 0
maqPuntos = 0

while(not salir):
	print("Quieres crear tu propia partida?(y/n)")
	propia = getch()
	while(True):
		if(propia == "y"):
			try:
				rangoMaximo = input("Introduce el numero maximo: ")
				rangoMinimo = input("Introduce el mumero minimo: ")
				if(rangoMaximo < 0 or rangoMinimo < 0):
					raise NameError
			except NameError:
				print "-->Error: Numero(s) no valido(s)"
				continue
			except SyntaxError:
				print "-->Error: Numero(s) no introducido(s)"
				continue

		else:
		    rangoMaximo = 100
		    rangoMinimo = 0
		for x in range (1,20):
		    if(math.pow(2,x) > rangoMaximo):
			numero_intentos = x-1
			break
		    else:
			numero_intentos = x
			numero_int_inicial = x
		factorPista = int(pow(2,x))/10
		try:
			number = random.randrange(rangoMinimo,rangoMaximo)
		except ValueError:
			print("->Error: Tiene que ser un numero entero")
			continue
		print "Intente adivinar el numero entre " + str(rangoMinimo) + " y " + str(rangoMaximo)
		array=[]
		resumenMenor=[]
		resumenMayor=[]
		print "Tienes",numero_intentos,"intentos"
		jugando = True
		minimo = rangoMinimo
		maximo = rangoMaximo
		break
	while jugando:

		try:
			intento = int(raw_input("Numero: "))
		except SyntaxError:
			print "->Error: Numero no introducido"
			continue
		except ValueError:
			print "->Error: Numero no introducido"
			continue

		if((intento< rangoMinimo)or(intento > rangoMaximo)):
		        print "Rango equivocado"
		        print "El rango es de",rangoMinimo,"a",rangoMaximo
			continue
		elif(intento > number):
			print "El numero es menor"
			array.append("MENOR que " + str(intento))
			numero_intentos = numero_intentos-1
		elif(intento< number):
			print "El numero es mayor"
			array.append("MAYOR que " + str(intento))
			numero_intentos = numero_intentos-1
		elif(intento == number):
			premio = 1
			misPuntos +=1
			print "Enhorabuena!, has ganado " + str(premio) + " punto"
			jugando = False

		if(numero_intentos < 1):
		    jugando = False

		if(jugando):
	     		print "-------Resumen:-------"
	     		print "|Te quedan",numero_intentos,"intentos|"

			for x in array:
				mo = re.match("(MAYOR|MENOR)\s+que\s+(\d+)",x)
				if(mo.group(1) == "MENOR"):
					valor = mo.group(2)
					if(valor not in resumenMenor):
						resumenMenor.append(valor)
						for y in resumenMenor:
							if(int(y) < int(maximo)):
								maximo = y
					#coger el numero a un array de mayores y coger el menor

				else:
					valor = mo.group(2)
					if(valor not in resumenMayor):
						resumenMayor.append(valor)
						for y in resumenMayor:
							if(int(y) > int(minimo)):
								minimo = y
					#coger el numero a un array de menores y coger el mayor
				#sacar los dos valores
			print ("MAYOR que " + str(minimo) + ", MENOR que " + str(maximo))
			#Condicion antigua 
			#if(0.3 * random.randrange(1.0,10.0) < 1.0):
			#Condicion a poner 
			if(math.fabs(number - intento) > (rangoMaximo-rangoMinimo)/(numero_intentos-(numero_int_inicial-numero_intentos-1))):
				
				#PISTAS				
				print(" Quieres una pista?(y/n)")
				pista = getch()
				if(pista == "y"):
					limiteInferior = number-random.randrange(0,numero_intentos*factorPista)
					limiteSuperior = random.randrange(0,numero_intentos*factorPista)+number
					if(random.randrange(0,10) > 0.5):
						array.append("|MAYOR que " + str(limiteInferior) +"|")
						print("|MAYOR que " + str(limiteInferior))
					else:
						array.append("|MENOR que " + str(limiteSuperior) + "|")
						print("|MAYOR que " + str(limiteSuperior))

					#Tratamiento de valores menores que rangoMinimo y mayores que rangoMaximo
					if(limiteInferior < rangoMinimo):
						limiteInferior = rangoMinimo
					if(limiteSuperior > rangoMaximo):
						limiteSuperior = rangoMaximo

					numero_intentos -= 1
					print("Se te resta 1 intento, te quedan " + str(numero_intentos) + " intentos")
		     			if(numero_intentos < 1):
		    				jugando = False
		if(not jugando):
		    if(numero_intentos != 0):
			       print "Te quedaban solo", numero_intentos,"intentos"
		    else:
			print "Te quedaste sin intentos"
			maqPuntos += 1
		    print "El numero era", number
	print("Llevas " + str(misPuntos) +" puntos y la maquina lleva " + str(maqPuntos) + " puntos")

	print("Quieres jugar otra vez?(y/n)")
	varSalir = getch()
	if(varSalir == "y"):
		salir = False
	else:
		salir = True

if(misPuntos > maqPuntos):
	print("Has ganado a la maquina")
elif(misPuntos == maqPuntos):
 print("Has empatado")
else:
	print("La maquina ha conseguido mas puntos que tu")
