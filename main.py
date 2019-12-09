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
			player_one = Player()
			player_two = PlayerAI()
			gameThread(player_one, player_two)
		elif(userOption == 2):
			print("Two players mode running ...")
			player_one = Player()
			player_two = Player()
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
		print(player_one.numbers)
		print(player_two.numbers)
		players_list[nextTurn(turn)].tryShot(players_list[turn].shot())
		if(players_list[nextTurn(turn)].isAlive() == False):
			running = False
			print("Player",turn,"wins!")
		else:
			turn = nextTurn(turn)

def nextTurn(turn):
	return (turn+1)%2

def generateRandomList():
	numbers = random.sample(range(10),5)
	return numbers
		
#----------------------- PLAYER CLASS ---------------------------------------------------
class Player(object):
	numbers = random.sample(range(10),5)
	def __init__(self):
		print("Human Player created ...")
        
	@classmethod
	def tryShot(self, number):
		if number in self.numbers:
			self.numbers[self.numbers.index(number)] = -1

	@classmethod
	def isAlive(self):
		cont = 0
		for x in range(5):
			if self.numbers[x]==-1:
				cont+=1
		return cont!=5

	@classmethod
	def shot(self):
        	return int(input("SHOT! -> "))
    
#----------------------------------------------------------------------------------------
#------------------------ PLAYER-AI CLASS ------------------------------------------------
class PlayerAI(object):
	numbers = random.sample(range(10),5)
	def __init__(self):
		print("AI Player created ...")
	
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

	@classmethod
	def shot(self):
        	return random.randint(0,11)
#----------------------------------------------------------------------------------------
mainMenu()
