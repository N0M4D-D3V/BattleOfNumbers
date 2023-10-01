import random

class Player:
	numbers = random.sample(range(10),5)

	def __init__(self):
		print(self.numbers)
		
	@classmethod
	def tryShot(self, number):
		if number in self.numbers:
			self.numbers[self.numbers.index(number)] = -1
			return True
		else:
			return False

	@classmethod
	def isAlive(self):
		cont = 0
		for x in range(5):
			if self.numbers[x]==-1:
				cont+=1
		return cont!=5

Prueba = Player()
print(Prueba.tryShot(5))
print(Prueba.isAlive())
print(Prueba.numbers)
