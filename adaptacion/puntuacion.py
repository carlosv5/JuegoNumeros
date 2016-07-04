#!/usr/bin/python
import math
class Score:
    """Score class"""

    def __init__(self, minNumber, maxNumber):
        self.playerPts = 0
	self.machPts = 0
	self.intentos = self.calcularIntentos(minNumber, maxNumber)

    def machPoint(self):
	self.machPts = self.matchPts + 1 

    def playerPoint(self):
	self.playerPts = self.playerPts + 1 

    def calcularIntentos(self, minNumber, maxNumber):
        for x in range (1,20):
            if(math.pow(2,x) > maxNumber):
                self.intentos = x-1
                break
            else:
                self.intentos = x
        return self.intentos
	
