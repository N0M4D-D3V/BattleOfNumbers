import random

class Player(object):

	def __init__(self):
		global numbers
		for x in range(5):
			numbers.append(random.randint(1,10))
			print(numbers)	

	@classmethod
	def tryShot(self, number):
		if number in numbers:
			print("Golpeado")

	@classmethod
	def isAlive(self):
		cont = 0
		for x in numbers:
			if numbers[x]==-1:
				cont+=1
		print(cont)

Prueba = Player()
