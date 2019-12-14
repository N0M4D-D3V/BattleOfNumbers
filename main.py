import random

def mainMenu():
	running = True
	player_one=Player()
	player_two=Player()
	player_ai=PlayerAI()

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
			player_one.reload()
			player_ai.reload()
			gameThread(player_one, player_ai)
		elif(userOption == 2):
			print("Two players mode running ...")
			player_one.reload()
			player_two.reload()
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
		print(">< Player",turn,"><",end="\n\r\n\r")
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
		
#----------------------- PLAYER CLASS ---------------------------------------------------
class Player(object):
	numbers = []
	def __init__(self):
		print("Human Player created ...")
	@classmethod
	def tryShot(self, number):
		if number in self.numbers:
			self.numbers[self.numbers.index(number)] = -1
			print("\n\r... HITTED!\n\r")
	@classmethod
	def isAlive(self):
		return self.numbers.count(-1)!=5
	@classmethod
	def shot(self):
		try:
			shot = int(input("SHOT! -> "))
		except ValueError:
			print("ValueError D:! ")
			shot = 0
		finally:
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
	@classmethod
	def reload(self):
		self.numbers = random.sample(range(10),5)
#----------------------------------------------------------------------------------------
#------------------------ PLAYER-AI CLASS ------------------------------------------------
class PlayerAI(object):
	numbers = []
	numbersShoted = []
	def __init__(self):
		print("AI Player created ...")
	@classmethod
	def tryShot(self, number):
		if number in self.numbers:
			self.numbers[self.numbers.index(number)] = -1
			print("\n\r... HITTED!\n\r")
	@classmethod
	def isAlive(self):
		return self.numbers.count(-1)!=5
	@classmethod
	def shot(self):
		shot = random.randint(0,11)
		while(shot in self.numbersShoted):
			shot = random.randint(0,11)
		self.numbersShoted.append(shot)
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
	@classmethod
	def reload(self):
		self.numbers = random.sample(range(10),5)
		numbersShoted = []
#----------------------------------------------------------------------------------------
mainMenu()
