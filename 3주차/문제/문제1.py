import random

def dice_game():
    keep_go = 'Y'
    while keep_go == 'Y':
        player, computer = random.randint(1, 6), random.randint(1, 6)
        print(f'인간: 주사위값 = {player}')
        print(f'컴퓨터: 주사위값 = {computer}')
        
        if player < computer:
            print('컴퓨터 승리')
        elif player > computer:
            print('인간 승리')
        else:
            print('무승부')
        
        keep_go = input('중단할까요? Y/N')

dice_game()
