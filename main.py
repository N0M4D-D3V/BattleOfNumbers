import random

def mainMenu():
	running = True
	while(running):
		print("")
		print("<>---<>---<> BATTLE OF NUMBERS <>---<>---<>")
		print(" |   <>---<>    ONE PLAYER     <>---<>   | ")
		print(" |   <>---<>    TWO PLAYERS    <>---<>   | ")
		print(" |   <>---<>       EXIT        <>---<>   | ")
		print(" *\_____________________________________/* ")
		print("")
		userOption = int(input("Choose an option: "))
		if(userOption == 1):
			print("One player mode running ...")
			player_one = Player(generateRandomList())
			player_two = PlayerAI(generateRandomList())
			gameThread(player_one, player_two)
		elif(userOption == 2):
			print("Two players mode running ...")
			player_one = Player(generateRandomList())
			player_two = Player(generateRandomList())
			gameThread(player_one, player_two)
		elif(userOption == 3):
			print("Good bye bitch !")
			running = False
		else:
			print("Yeah? Good")
			running = False
def gameThread(player_one, player_two):
	running = True
	players_list = [player_one,player_two]
	turn = 0
	while(running):
		print(">< Player",turn,"><")
		print(player_one)
		print(player_two)
		players_list[nextTurn(turn)].tryShot(players_list[turn].shot())
		if(players_list[nextTurn(turn)].isAlive() == False):
			running = False
			print("Player",turn,"wins!")
		else:
			turn = nextTurn(turn)
def nextTurn(turn):
	return (turn+1)%2

def generateRandomList():
	return random.sample(range(10),5)
		
#----------------------- PLAYER CLASS ---------------------------------------------------
class Player(object):
	numbers = random.sample(range(10),5)
	def __init__(self, randomSample):
		self.numbers = randomSample
		print("Human Player created ...")
	@classmethod
	def tryShot(self, number):
		if number in self.numbers:
			self.numbers[self.numbers.index(number)] = -1
			print("... HITTED!")
	@classmethod
	def isAlive(self):
		return self.numbers.count(-1)!=5
	@classmethod
	def shot(self):
        	return int(input("SHOT! -> "))
	@classmethod
	def __str__(self):
		ocult_values = "["
		for x in range(5):
			if self.numbers[x]==-1:
				ocult_values = ocult_values + " X"
			else:
				ocult_values = ocult_values + " ?"
		ocult_values = ocult_values + " ]"
		return ocult_values
#----------------------------------------------------------------------------------------
#------------------------ PLAYER-AI CLASS ------------------------------------------------
class PlayerAI(object):
	numbers = random.sample(range(10),5)
	def __init__(self, randomSample):
		self.numbers = randomSample
		print("AI Player created ...")
	@classmethod
	def tryShot(self, number):
		if number in self.numbers:
			self.numbers[self.numbers.index(number)] = -1
			print("... HITTED!")
	@classmethod
	def isAlive(self):
		return self.numbers.count(-1)!=5
	@classmethod
	def shot(self):
		shot = random.randint(0,11)
		print("SHOT! -> ",end="")
		print(shot)
		return shot
	@classmethod
	def __str__(self):
		ocult_values = "["
		for x in range(5):
			if self.numbers[x]==-1:
				ocult_values = ocult_values + " X"
			else:
				ocult_values = ocult_values + " ?"
		ocult_values = ocult_values + " ]"
		return ocult_values
#----------------------------------------------------------------------------------------
mainMenu()
