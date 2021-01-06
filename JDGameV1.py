print("Please choose an option (rock, scissors or paper)?:")
continue_play = True

def continueGame():
    response = str(input('Do you want to play another game, yes or no?\n')).lower().strip()
    return response=='yes'

while continue_play:
    options_dic = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_1 = str(input("Player 1: ")).lower().strip()
    player_2 = str(input("Player 2: ")).lower().strip()
    player1Value = options_dic.get(player_1)
    player2Value = options_dic.get(player_2)
    resultDifference = player1Value - player2Value

    if resultDifference in [-1, 2]:
        print('Player 1 wins.')
        continue_play= continueGame()
    elif resultDifference in [-2, 1]:
        print('player 2 wins.')
        continue_play= continueGame()
    else:
        print('Draw. Play Again!\n')