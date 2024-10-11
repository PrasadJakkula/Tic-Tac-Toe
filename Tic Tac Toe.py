import random
markings = {'1':' ','2':' ','3':' ',
'4':' ','5':' ','6':' ',
'7':' ','8':' ','9':' '
}
#The board and to show it on screen.
def show_board(markings):
	print("   "+"|"+"   "+"|"+"  ")
	print(" "+markings['1']+" "+"|"+" "+markings['2']+" "+"|"+" "+markings['3']+" ")
	print("   "+"|"+"   "+"|"+"   ")
	print("---+---+---")
	print("   "+"|"+"   "+"|"+"   ")
	print(" "+markings['4']+" "+"|"+" "+markings['5']+" "+"|"+" "+markings['6']+" ")
	print("   "+"|"+"   "+"|"+"   ")
	print("---+---+---")
	print("   "+"|"+"   "+"|"+"   ")
	print(" "+markings['7']+" "+"|"+" "+markings['8']+" "+"|"+" "+markings['9']+" ")
	print("   "+"|"+"   "+"|"+"   ")
print("These are the available moves.")
available_moves = ['1','2','3','4','5','6','7','8','9']
players_move = []
ai_move = []
print(available_moves)
	

#Ask for the word they like.
user_word = input('Please enter your word("X"/"O"): ').upper()
ai_word = "O" if user_word == "X" else "X"

#Asking the users move and removing it from available moves and storing it in players move.
def player():
	while True:
		your_move = input("Please select the box that you want to place your word from available boxes.")
		if your_move in available_moves:
			markings[your_move]=user_word
			players_move.append(your_move)
			available_moves.remove(your_move)
			show_board(markings)
			print("you choose the box "+your_move)
			print("The available moves now are")
			print(available_moves)
			break
		else:
			print("Invalid move please try again.")

#ai move that is selecting the random move from availble move.
def ai():
	a = random.choice(available_moves)
	markings[a]=ai_word
	available_moves.remove(a)
	show_board(markings)
	ai_move.append(a)
	print("ai choose box "+str(a))
	print("Now the available moves are")
	print(available_moves)

#def choose the winner.
def winner():
	winning_combinations = [
	['1','2','3'],['4','5','6'],['7','8','9'],
	['1','4','7'],['2','5','8'],['3','6','9'],
	['1','5','9'],['3','5','7']
	]
	for combination in winning_combinations:
		if all(pos in players_move for pos in combination):
			print("You won the game")
			return True
		elif all(pos in ai_move for pos in combination):
			print("Ai won the game")
			return True
	return False
			
#The main game while loop.
def main_game():
	
	for value in range(5):
		player()
		if winner():
			break
		if not available_moves:
			print("Its a tie.")
			break
		ai()
		if winner():
			break
main_game()

