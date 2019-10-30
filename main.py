#------ global variable-------

# game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#if game is going
game_on = True

# winner and losser
winner = None

#defining whose turn it is
current_player = "x"

def play_game():
  print("Welcome to the Game!")
  #display initial board
  display_board()

  while game_on:
    handle_turn(current_player)
    checkIf_game_on()
    flip_player()

  # the game has ended
  if winner == "x" or winner == "o":
    print(winner + " won! ")
  elif winner == None:
    print(" Its a tie ")

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] )
  print(board[3] + " | " + board[4] + " | " + board[5] )
  print(board[6] + " | " + board[7] + " | " + board[8] )


def checkIf_game_on():
  checkIf_win()
  checkIf_tie()

def checkIf_win():
  # declare global variable
  global winner
  # check rows columns diagoinals
  row_win = row_winner()
  column_win = column_winner()
  diagonal_win = diagonal_winner()

  if row_win:
    winner = row_win
  elif column_win:
    winner = column_win
  elif diagonal_win:
    winner = diagonal_win
  else:
    winner = None

  return

def row_winner():
  #setup global variable
  global game_on
  #check for same values of rows
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if a win occur, stop the game
  if row_1 or row_2 or row_3:
    game_on = False
  #determine who is the winner 'x' or 'o'
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

  return

def column_winner():
  #setup global variable
  global game_on
  #check for same values of rows
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  #if a win occur, stop the game
  if column_1 or column_2 or column_3:
    game_on = False
  #determine who is the winner 'x' or 'o'
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  
  return

def diagonal_winner():
  #setup global variable
  global game_on
  #check for same values of rows
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  #if a win occur, stop the game
  if diagonal_1 or diagonal_2:
    game_on = False
  #determine who is the winner 'x' or 'o'
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  
  return

def checkIf_tie():
  global game_on
  # stoping game in case of a tie
  if "-" not in board:
    game_on = False

  return

def flip_player():
  global current_player
  # switching between players
  if current_player == "x":
    current_player = "o"
  else:
    current_player = "x"

  return

def handle_turn(current_player):
  print("\n" + current_player + "'s turn ")
  position = input("choose a position from 1-9: ")

  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("postion not empty, try another one")

  board[position] = current_player
  display_board()

play_game()





# reuirements
# board - display
# play game
# check win
# check tie
# flip player
