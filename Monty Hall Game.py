import random

#############################
# MONTY HALL MAIN FUNCTION  #
#############################

def monty(n):
    car = random.randint(1, 3)
    for i in range(1,4):
        if i == car:
            continue
        else:
            goat1 = i
            break
    for i in range(1,4):
        if i == car or i == goat1:
            continue
        else:
            goat2 = i
            break
    seq = (goat1, goat2)
    print('A goat is revealed to be behind door..')
    if n == car:
        ran = random.choice(seq)
        print(ran)
        x = ran
    elif n == goat1:
        print(goat2)
        x = goat2
    elif n == goat2:
        print(goat1)
        x = goat1
    ans = str(input('Do you want to switch? Input y or n: '))
    while ans not in ('y', 'n'):
        ans = str(input('Please be a bit more serious, two goats are at stake. Switch, y or n: '))
    if ans == 'y':
        for i in range(1,4):
            if i == n or i == x:
                continue
            else:
                swap = i
                break
        if swap == car:
            print('Congrats! You win a car!')
            print('   /__________ ')
            print(' [ (_) ____ (_)] ')
        elif swap == goat1 or swap == goat2:
            print('Goat. Thanks for playing!')
    elif ans == 'n':
        if n == car:
            print('Congrats! You win a car!')
            print('   /__________ ')
            print(' [ (_) ____ (_)] ')
        elif n == goat1 or n == goat2:
            print('Goat. Thanks for playing!')
            
#############################################################################
play = True
while play:
    print('##############################################################################')
    print('Welcome to the Monty Hall Game! There are 3 doors: Door 1, Door 2, Door 3.')
    print('One door will contain a car! The other two doors contain goats.')
    print('##############################################################################')
    #name = str(input('What is our contestant\'s name? '))
    #print('Welcome to the game, ' + name + '!')
    player = int(input('Choose your door: '))
    while player not in (1, 2, 3):
            player = int(input('No such door, please choose again: '))
    monty(player)
    if input('Play again? Input y or n: ') == 'n':
        play = False

if play == False:
    print('===========================================================')
    print('Monty Hall Game (Shitty Python version) programmed by Andy')
    print('===========================================================')
