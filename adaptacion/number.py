#!/usr/bin/python
import random
class Number:
    """Number class"""


    def calculateNumber(self, minNumber, maxNumber):
        return random.randrange(minNumber,maxNumber)

    def __init__(self, minNumber, maxNumber):
        self.minNumber = minNumber
        self.maxNumber = maxNumber
	self.number = self.calculateNumber(minNumber, maxNumber)



