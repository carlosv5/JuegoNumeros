#!/usr/bin/python
import random
print "Bienvenido al juego"
print "Intente adivinar el numero"
rangoMaximo = 101
rangoMinimo = 1
puntos = 10
r = random.randrange(rangoMinimo,rangoMaximo)
numero_intentos = 5
array=[]
print "Tienes",numero_intentos,"intentos y " + str(puntos) + " puntos"
jugando = True
while jugando:
	intento = input("Numero:")
	if((intento< rangoMinimo)or(intento > rangoMaximo)):
                print "Rango equivocado"
                print "El rango es de",rangoMinimo,"a",rangoMaximo
		continue
	elif(intento > r):
		print "El numero es menor"
		array.append("El numero es menor que " + str(intento))
		numero_intentos = numero_intentos-1
	elif(intento< r):
		print "El numero es mayor"
		array.append("El numero es mayor que " + str(intento))
		numero_intentos = numero_intentos-1
	elif(intento == r):
		print "El numero era",intento
		jugando = False
			
	if(numero_intentos < 1):
	    jugando = False

	if(jugando):
     		print "Resumen:"
		puntos -= 1
     		print "Te quedan",numero_intentos,"intentos y " + str(puntos) + " puntos"

		for x in array:
	        	print x
		if(0.3 * random.randrange(1.0,10.0) < 1.0):
			pista = raw_input("Quieres una pista(y/n): ")
			if(pista == "y"):
				print("El numero que buscas esta entre " + str(r-random.randrange(0,numero_intentos*10)) + " y " + str(random.randrange(0,numero_intentos*10)+r))
				puntos -=2
				print("Se te restan 2 puntos, te quedan " + str(puntos) + " puntos")
	     
	else:
		print "Te quedaban solo", numero_intentos,"intentos"
		premio = 90
		print "Enhorabuena!, has ganado " + str(puntos+premio) + " puntos"
		print "El numero era", r
