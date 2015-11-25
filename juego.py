#!/usr/bin/python
import random
print "Bienvenido al juego"
print "Intente adivinar el numero"
rangoMaximo = 101
rangoMinimo = 1
r = random.randrange(rangoMinimo,rangoMaximo)
numero_intentos = 5
array=[]
print "Tienes",numero_intentos,"intentos"
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
     		print "Te quedan",numero_intentos,"intentos"
	     	for x in array:
	        	print x
	else:
		print "Te quedaban solo", numero_intentos,"intentos"
		print "El numero era", r
