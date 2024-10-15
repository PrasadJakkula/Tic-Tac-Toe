import random
markings = {'1':' ','2':' ','3':' ',
'4':' ','5':' ','6':' ',
'7':' ','8':' ','9':' '
}
def show_board(markings):
	#Showing the board.
	print("   "+"|"+"   "+"|"+"   ")
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

available_moves = ['1','2','3','4','5','6','7','8','9']
movesofplayer = []
movesofai = []

print('\t\t\tWelcome to the game \n\t\t\t\tof \n\t\t\t   "TIC TAC TOE"')

#Asking for user if they want to play with their friend or computer.
while True:
	user_playing = input("Please enter your choice with whome you want to play the game \n1.friend \n2.computer.")
	if user_playing == '1':
		opponent = 'friend'
		break
	elif user_playing == '2':
		opponent = 'computer'
		break
	else:
		print("Please enter only numbers.")
		
#Now ask for user what word they want.
while True:
	user_word = input("Please select your word between('X'/'O'): ").upper()
	if user_word == 'X':
		print("You choose word",user_word)
		ai_word = 'O'
		print("Ai's word is",ai_word)
		break
	elif user_word == 'O':
		print("You choose word",user_word)
		ai_word = 'X'
		print("Ai's word is",ai_word)
		break
	else:
		print("Please enter the choice between  ('X'/'O')")

#Taking the players word and adding them to the box.	
def players_move():
	players_word = input("Please enter the box number in which you want to place your word.")
	if players_word in available_moves:
		markings[players_word] = user_word
		available_moves.remove(players_word)
		show_board(markings)
		movesofplayer.append(players_word)
		print("Player1 choose box "+players_word)
		print("Now the available moves are")
		print(available_moves)
			
	else:
		return players_move()

#Opponents move for the game play.
def opponent_move():
		###If user choose to play with friend then this code will be activated.
		if user_playing == '1':
			friend_move = input("Please enter the player 2 move")
			if friend_move in available_moves:
				markings[friend_move]=ai_word
				available_moves.remove(friend_move)
				show_board(markings)
				movesofai.append(friend_move)
				print("Player2 choose box",friend_move)
				print("Now the available moves are")
				print(available_moves)

		###If user choose to play with computer then this code will be executed			
		elif user_playing == '2':
			if not movesofai:
				a = random.choice(available_moves)
				markings[a]=ai_word
				available_moves.remove(a)
				show_board(markings)
				movesofai.append(a)
				print("Ai choose the box",str(a))
				print('Now the available moves are')
				print(available_moves)
			else:
				#This is the move of ai to win the game.
				if '1' in available_moves and '2' in movesofai and '3' in movesofai:
					a = '1'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#This is the move of ai to win the game.
				elif '2' in available_moves and '1' in movesofai and '3' in movesofai:
					a = '2'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '3' in available_moves and '1' in movesofai and '2' in movesofai:
					a = '3'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win if possoble.
				elif '4' in available_moves and '5' in movesofai and '6' in movesofai:
					a = '4'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win if possible.
				elif '5' in available_moves and '4' in movesofai and '6' in movesofai:
					a = '5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win if possible.
				elif '6' in available_moves and '4' in movesofai and '5' in movesofai:
					a= '6'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win if possible.
				elif '7' in available_moves and '8' in movesofai and '9' in movesofai:
					a = '7'
					markings[a] = ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win if possible.
				elif '8' in available_moves and '7' in movesofai and '9' in movesofai:
					a = '8'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print('Ai choose the box',str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '9' in available_moves and '7' in movesofai and '8' in movesofai:
					a = '9'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '1' in available_moves and '4' in movesofai and '7' in movesofai:
					a = '1'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '4' in available_moves and '1' in movesofai and '7' in movesofai:#This is the move of ai to win the game.
					a = '4'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				elif '7' in available_moves and '1' in movesofai and '4' in movesofai:
					a = '7'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '2' in available_moves and '5' in movesofai and '8' in movesofai:
					a = '2'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '5' in available_moves and '2' in movesofai and '8' in movesofai:
					a = '5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '8' in available_moves and '2' in movesofai and '5' in movesofai:
					a = '8'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win.
				elif '3' in available_moves and '6' in movesofai and '9' in movesofai:
					a = '3'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '6' in available_moves and '3' in movesofai and '9' in movesofai:
					a = '6'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are",str(a))
					print(available_moves)
				#move of ai to win.
				elif '9' in available_moves and '3' in movesofai and '6' in movesofai:
					a = '9'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '1' in available_moves and '5' in movesofai and '9' in movesofai:
					a = '1'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '5' in available_moves and '1' in movesofai and '9' in movesofai:
					a ='5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '9' in available_moves and '1' in movesofai and '5' in movesofai:
					a = '9'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '3' in available_moves and '5' in movesofai and '7' in movesofai:
					a = '3'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to win
				elif '5' in available_moves and '3' in movesofai and '7' in movesofai:
					a = '5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#moves of ai to win
				elif '7' in available_moves and '3' in movesofai and '5' in movesofai:
					a= '7'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#This is the move of ai to defend.
				elif '1' in available_moves and '2' in movesofplayer and '3' in movesofplayer:
					a = '1'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box "+str(a))
					print("Now the available moves are")
					print(available_moves)
				#This is the move of ai to defend.	
				elif '2' in available_moves and '1' in movesofplayer and '3' in movesofplayer:
					a = '2'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box "+str(a))
					print("Now the available moves are")
					print(available_moves)
				#Moves of ai to defend.
				elif '3' in available_moves and '1' in movesofplayer and '2' in movesofplayer:
					a = '3'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("NOw the available moves are")
					print(available_moves)
				#Moves of ai to defend
				elif '4' in available_moves and '5' in movesofplayer and '6' in movesofplayer:
					a = '4'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '5' in available_moves and '4' in movesofplayer and '6' in movesofplayer:
					a = '5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '6' in available_moves and '4' in movesofplayer and '5' in movesofplayer:
					a = '6'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the availble moves are")
					print(available_moves)
				#move of ai to defend.
				elif '7' in available_moves and '8' in movesofplayer and '9' in movesofplayer:
					a = '7'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '8' in available_moves and '7' in movesofplayer and '9' in movesofplayer:
					a = '8'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend
				elif '9' in available_moves and '7' in movesofplayer and '8' in movesofplayer:
					a = '9'
					markings[a] = ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '1' in available_moves and '4' in movesofplayer and '7' in movesofplayer:
					a = '1'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				elif '4' in available_moves and '1' in movesofplayer and '7' in movesofplayer:#This is the move of ai to defend if it cannot win.
					a = '4'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print('Ai choose the box',str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '7' in available_moves and '1' in movesofplayer and '4' in movesofplayer:
					a = '7'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '2' in available_moves and '5' in movesofplayer and '8' in movesofplayer:
					a = '2'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '5' in available_moves and '2' in movesofplayer and '8' in movesofplayer:
					a = '5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#move of ai to defend
				elif '8' in available_moves and '2' in movesofplayer and '5' in  movesofplayer:
					a = '8'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend.
				elif '3' in available_moves and '6' in movesofplayer and '9' in movesofplayer:
					a = '3'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend
				elif '6' in available_moves and '3' in movesofplayer and '9' in movesofplayer:
					a = '6'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#move of ai to defend
				elif '9' in available_moves and '3' in movesofplayer and '6' in movesofplayer:
					a = '9'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend
				elif '1' in available_moves and '5' in movesofplayer and '9' in movesofplayer:
					a = '1'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#move of ai to defend
				elif '5' in available_moves and '1' in movesofplayer and '9' in movesofplayer:
					a = '5'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend
				elif '9' in available_moves and '1' in movesofplayer and '5' in movesofplayer:
					a = '9'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend
				elif '3' in available_moves and '5' in movesofplayer and '7' in movesofplayer:
					a = '3'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				#Move of ai to defend
				elif '5' in available_moves and '3' in movesofplayer and '7' in movesofplayer:
					a = '5'
					markings[a]=ai_word
					available_move.remove(a)
					show_board(a)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are",str(a))
					print(available_moves)
				#moves of ai to defend	
				elif '7' in available_moves and '3' in  movesofplayer and '5' in movesofplayer:
					a = '7'
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves)
				else:
					a = random.choice(available_moves)
					markings[a]=ai_word
					available_moves.remove(a)
					show_board(markings)
					movesofai.append(a)
					print("Ai choose the box",str(a))
					print("Now the available moves are")
					print(available_moves) 
		
		
#Deciding who wins the game.
def winner():
	winning_combination = [
	['1','2','3'],['4','5','6'],['7','8','9'],
	['1','4','7'],['2','5','8'],['3','6','9'],
	['1','5','9'],['3','5','7']
	]
	for combination in winning_combination:
		if all(pos in movesofplayer for pos in combination):
			print("You won the game.")
			return True
		elif all(pos in movesofai for pos in combination):
			if user_playing == '1':
				print("Player 2 won the game. ")
				return True
			else:
				print("Ai won the game.")
				return True
	return False
	
#Main game loop for the game.
def main_game():
	for value in range(5):
		players_move()
		if winner():
			break
		if not available_moves:
			print("Its a tie")
			break
		opponent_move()
		if winner():
			break
		
	
main_game()

