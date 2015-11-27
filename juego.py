#!/usr/bin/python
import random
import math

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
		    rangoMinimo = 1
		for x in range (1,20):
		    if(math.pow(2,x) > rangoMaximo):
			numero_intentos = x-1
			break
		    else:
			numero_intentos = x
		try:
			number = random.randrange(rangoMinimo,rangoMaximo)
		except ValueError:
			print("->Error: Tiene que ser un numero entero")
			continue
		print "Intente adivinar el numero entre " + str(rangoMinimo) + " y " + str(rangoMaximo)
		array=[]
		print "Tienes",numero_intentos,"intentos"
		jugando = True
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
			array.append("El numero es menor que " + str(intento))
			numero_intentos = numero_intentos-1
		elif(intento< number):
			print "El numero es mayor"
			array.append("El numero es mayor que " + str(intento))
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
				print "|" + x + "|"
			if(0.3 * random.randrange(1.0,10.0) < 1.0):
				print(" Quieres una pista?(y/n)")
				pista = getch()
				if(pista == "y"):
					print("|El numero que buscas esta entre " + str(number-random.randrange(0,numero_intentos*5)) + " y " + str(random.randrange(0,numero_intentos*5)+number)+"|")
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
