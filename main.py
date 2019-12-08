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
		print(player_one.numbers)
		print(player_two.numbers)
		
		players_list[nextTurn(turn)].tryShot(int(input("SHOT! ")))
		if(players_list[nextTurn(turn)].isAlive() == False):
			running = False
		turn = nextTurn(turn)

def nextTurn(turn):
	return (turn+1)%2
		
#----------------------- PLAYER CLASS ---------------------------------------------------
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
#----------------------------------------------------------------------------------------
mainMenu()
