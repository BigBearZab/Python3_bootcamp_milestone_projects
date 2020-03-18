# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:17:20 2020

@author: denis
"""
#%%
#input player 1 choice


def player_choice():
    global p1 #saves who is playing as what
    global p2
    global firstturn
    global secondturn
    play_1_ch = input("Player 1, would you like to be Xs or Os? ")
    if play_1_ch == 'O' or play_1_ch =='o':
        p1 = 'O'
        p2 = 'X'
        firstturn = 'Player 1'
        secondturn = 'Player 2'
        print('Player 1 goes first with Os')
    else:
        p1 = 'X'
        p2 = 'O'
        firstturn = 'Player 2'
        secondturn = 'Player 1'
        print('Player 2 goes first with Os')
    print('Please input the location where you would like to place your token as on a mobile phone grid, example below.\nGet 3 in a row to win!')
    print("'1''2''3'\n'4''5''6'\n'7''8''9'")
        
player_choice()

#%%
#draw grid

#initialise blank grid
game_grid = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
tc = 1
def grid(inp=['',' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    l = [term for term in inp]
    print(f'Turn {tc}. The board lies below:')
    print(l[1:4])
    print(l[4:7])
    print(l[7:10])


grid(game_grid) #test input method

#%% Checker function, see if anyone has won

def statecheck(game_grid):
    global tc
    if tc % 2 == 0:
        var = 'X'
    else:
        var = 'O'
    if (game_grid[1] == game_grid[2] == game_grid[3] == var or game_grid[4] == game_grid[5] == game_grid[6] == var or game_grid[7] == game_grid[8] == game_grid[9] == var
        or game_grid[1] == game_grid[4] == game_grid[7] == var or game_grid[2] == game_grid[5] == game_grid[8] == var or game_grid[3] == game_grid[6] == game_grid[9] == var
        or game_grid[3] == game_grid[5] == game_grid[7] == var or game_grid[1] == game_grid[5] == game_grid[9] == var):

        return True
    else:
#        tc +=1
#        print(f'Play continues to turn {tc}')
        return False



#%% Overall game
        
while tc <= 9:
    if tc % 2 == 0:
        var = 'X'
    else:
        var = 'O'
    if tc % 2 != 0:
        inp = input(f'{firstturn} please provide a location: ')
        game_grid[int(inp)] = var
        grid(game_grid)
        if statecheck(game_grid) == True:
            print(f'{firstturn} wins!')
            break
        else:
            tc +=1
            print(f'Play continues to turn {tc}')       
    else:
        inp = input(f'{secondturn} please provide a location: ')
        game_grid[int(inp)] = var 
        grid(game_grid)
        statecheck(game_grid)
        if statecheck(game_grid) == True:
            print(f'{secondturn} wins!')
            break
        else:
            tc +=1
            print(f'Play continues to turn {tc}')    
        
if tc == 10:
    print('No one wins, try again')
    

