
def mainMenu():
	running = True
	while(running):
		print("")
		print("<>------<>------<> BATTLE OF NUMBERS <>------<>------<>")
		print(" |      <>------<>    ONE PLAYER     <>------<>      | ")
		print(" |      <>------<>    TWO PLAYERS    <>------<>      | ")
		print(" |      <>------<>       EXIT        <>------<>      | ")
		print(" *\_________________________________________________/* ")
		print("")

		userOption = int(input("Choose an option: "))
	
		if(userOption == 1):
			print("One player mode running ...")
		elif(userOption == 2):
			print("Two players mode running ...")
		elif(userOption == 3):
			print("Good bye bitch !")
			running = False
		else:
			print("Yeah? Good")
			running = False

mainMenu()
