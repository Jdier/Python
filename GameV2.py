print("Please choose an option (rock, scissors or paper)?:")
continue_play = True

def continueGame():
    response = str(input('Do you want to play another game, yes or no?\n')).lower().strip()
    return response=='yes'

while continue_play:
    
    player_1 = str(input("Player 1: ")).lower().strip()
    player_2 = str(input("Player 2: ")).lower().strip()
    result=0
    if (player_1=='rock' and player_2=='scissors'):
        result=1
    elif (player_1=='rock' and player_2=='paper'):
        result=2
    elif (player_1=='rock' and player_2=='rock'):
        result=-1
    elif (player_1=='paper' and player_2=='rock'):
        result=1
    elif (player_1=='paper' and player_2=='scissors'):
        result=2
    elif (player_1=='paper' and player_2=='paper'):
        result=-1   
    elif (player_1=='scissors' and player_2=='rock'):
        result=1
    elif (player_1=='scissors' and player_2=='scissors'):
        result=-1
    elif (player_1=='scissors' and player_2=='paper'):
        result=2
    
    if (result ==  -1):
        print('Draw. Play Again!\n')
    elif (result == 1):
        print('player 1 wins.')
        continue_play= continueGame()
    elif (result == 2):
        print('player 2 wins.')
        continue_play= continueGame()
        
        