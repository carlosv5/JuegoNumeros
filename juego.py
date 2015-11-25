#!/usr/bin/python
import random
print "Bienvenido al juego"
rangoMaximo = 101
rangoMinimo = 1
r = random.randrange(rangoMinimo,rangoMaximo)
numero_intentos = 8
print "Tienes",numero_intentos,"intentos"
jugando = True
while jugando:
	print "Intente"
	intento = input("Numero:")
	if((intento< rangoMinimo)or(intento > rangoMaximo)):
                print "Rango equivocado"
                print "El rango es de",rangoMinimo,"a",rangoMaximo
		continue
	elif(intento > r):
		print "El numero es menor"
		numero_intentos = numero_intentos-1
	elif(intento< r):
		print "El numero es mayor"
                numero_intentos = numero_intentos-1
	elif(intento == r):
		print "El numero era",intento
		jugando = False
			
	if(numero_intentos < 1):
		jugando = False

	if(jugando):
  		print "Te quedan",numero_intentos,"intentos"
	else:
		print "Te quedaban solo", numero_intentos,"intentos"
		print "El numero era", r
