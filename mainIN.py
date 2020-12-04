""""
Program designed to train the Python programming language.
The program is simple and it is a game.
There are 3 red frogs and 3 blue frogs before the bridge, help to cross
the color of the blue frog across the bridge.
by: Paulo Victor Santos Magalhães
"""

from os import system

def lines(): # Function to represent lines
    print('-'*40)

# library that configures the colors of the letters
color = {'clean':'\033[m',
         'red':'\033[31m',
         'blue':'\033[34m'}

lines()
print(f'{"CROSSING GAME":^40}')
lines()

cont = 0

redFrog = [1,1,1] # Red frogs before the bridge
blueFrog = [2,2,2] # blue frogs before the bridge
redFrog2 = [0,0,0] # Red frogs after the bridge
blueFrog2 = [0,0,0] # Blue frogs after the bridge

try:
    print('There are 3 red frogs and 3 blue frogs before the bridge, help to cross the color of the blue frog to the other side of the bridge...')
    # Asks if the user wants to continue playing
    word = str(input('If you are ready to play type YES, if not type NO:  ')).strip().upper()
    while True:
        if word != 'NO' and word != 'YES':
            # Infinite loop until the decides whether to continue playing
            word = str(input('If you are ready to play type YES, if not type NO:  ')).strip().upper()
        else:
            break
    if word == 'YES':
        while True:
            # Game rule conditions, for frogs before the bridge
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0,3):
                    redFrog[c] = 1
                for c in range(0,3):
                    blueFrog[c] = 2
                for c in range(0,3):
                    redFrog2[c] = 0
                for c in range(0,3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 2 and blueFrog[2] == 0 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 2 and blueFrog[1] == 0 and blueFrog[2] == 0 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0

            if blueFrog[0] == 0 and blueFrog[1] == 2 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 2 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
                blueFrog2[2] = 0
            if blueFrog[0] == 2 and blueFrog[1] == 2 and blueFrog[2] == 0 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 0:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 2 and blueFrog[2] == 0 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 0:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 2 and blueFrog[1] == 0 and blueFrog[2] == 0 and redFrog[0] == 1 and redFrog[1] == 1 and redFrog[2] == 0:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                   redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 0 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 0 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 1 and redFrog[1] == 0 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 0 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 0 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0
            if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 2 and redFrog[0] == 0 and redFrog[1] == 1 and redFrog[2] == 1:
                print('THERE ARE MORE RED FROGS THAN BLUE FROGS BEFORE THE BRIDGE... GAME RESTARTED...')
                for c in range(0, 3):
                    redFrog[c] = 1
                for c in range(0, 3):
                    blueFrog[c] = 2
                for c in range(0, 3):
                    redFrog2[c] = 0
                for c in range(0, 3):
                    blueFrog2[c] = 0


            lines()
            print('RULE: \nNo more red frogs than blue frogs are allowed before the bridge\nAll blue frogs must be after the bridge')
            print('CURRENT GAME:')
            
            print('{}Red frogs before the bridge: {}'.format(color['red'],color['clean']),end=' ')
            for c in range(0,3):
                print('{}{}{}'.format(color['red'],redFrog[c],color['clean']),end=' ')
            print('\n{}Blue frogs before the bridge: {}'.format(color['blue'],color['clean']),end=' ')
            for c in range(0, 3):
                print('{}{}{}'.format(color['blue'],blueFrog[c],color['clean']),end=' ')
            print('\n{}Red frogs after the bridge: {}'.format(color['red'],color['clean']),end=' ')
            for c in range(0, 3):
                print('{}{}{}'.format(color['red'],redFrog2[c],color['clean']),end=' ')
            print('\n{}Blue frogs after the bridge: {}'.format(color['blue'],color['clean']),end=' ')
            for c in range(0, 3):
                print('{}{}{}'.format(color['blue'],blueFrog2[c],color['clean']),end=' ')
            print(' ')
            lines()
            
            if blueFrog2[0] == 2 and blueFrog2[1] == 2 and blueFrog2[2] == 2:
                break
            # Decision if the user wnats to cross or bring the frog
            frog = int(input("\nType [1] to cross the frongs and [2] to bring the frogs back: "))
            while True:
                # Infinite loop until user decides whether to cross or bring the frog
                if frog != 1 and frog != 2:
                    frog = int(input("Type [1] to cross the frongs and [2] to bring the frogs back: "))
                else:
                    break
            if frog == 1:
                # Ask the user for the color of the frog to cross
                crossing = int(input('To cross the red frog type [1] and to cross the blue frog type [2]:  '))
                while True:
                    # Infinite loop until the user decides the color of the frog to cross
                    if crossing != 1 and crossing != 2:
                        crossing = int(input('To cross the red frog type [1] and to cross the blue frog type [2]:  '))
                    else:
                        break
                # Commands for crossing the red frog
                if crossing == 1:
                    while True:
                        if redFrog[0] == 0 and redFrog[1] == 0 and redFrog[2] == 0:
                            system('cls')
                            print('There are no red frogs to cross...')
                            break
                        if redFrog2[cont] == 0:
                            redFrog2[cont] = 1
                            redFrog[cont] = 0
                            cont = 0
                            system('cls')
                            break
                        else:
                            cont += 1
                # Blue frog crossing commands
                if crossing == 2:
                    while True:
                        if blueFrog[0] == 0 and blueFrog[1] == 0 and blueFrog[2] == 0:
                            system('cls')
                            print('There are no blue frogs to cross...')
                            break
                        if blueFrog2[cont] == 0:
                            blueFrog2[cont] = 2
                            blueFrog[cont] = 0
                            system('cls')
                            cont = 0
                            break
                        else:
                            cont += 1
            if frog == 2:
                    # Asks user to return frog color
                back  = int(input('Bring the type of red frog [1] and bring the type of blue frog [2]:   '))
                while True:
                        # Infinite loop until the user decides to return the frog color
                    if back != 1 and back != 2:
                        back = int(input('Bring the type of red frog [1] and bring the type of blue frog [2]:   '))
                    else:
                        break
                if back == 1:
                # commands for the return of the red frog
                        while True:
                            if redFrog2[0] == 0 and redFrog2[1] == 0 and redFrog2[2] == 0:
                                system('cls')
                                print('There are no red frogs to return...')
                                break
                            if redFrog2[cont] == 1:
                                redFrog2[cont] = 0
                                redFrog[cont] = 1
                                system('cls')
                                cont =  0
                                break
                            else:
                                cont += 1
                if back == 2:
                # blue frog return commands
                        while True:
                            if blueFrog2[0] == 0 and blueFrog2[1] == 0 and blueFrog2[2] == 0:
                                system('cls')
                                print('There are no red frogs to return...')
                                break
                            if blueFrog2[cont] == 2:
                                blueFrog2[cont] = 0
                                blueFrog[cont] = 2
                                system('cls')
                                cont = 0
                                break
                            else:
                                cont += 1
except Exception as error:
    print(f'ERROR...: {error.__class__}') # Messege that informs you if an error has occurred

else:
    if word == 'NO': # If the user types NO, the program will be terminated
        lines()
        print('SEE YOU LATER')
    else: # If the user enters YES, and ends the charllenge, will present this messege
        lines()
        print('END GAME... THANK YOU FOR PLAYING :)')

print('...')
