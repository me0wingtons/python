import random
import time

play = 1

while play:
    # difficulty #
    set = input('Select difficulty: easy, medium, hard, expert, legendary : ')

    # initiate #
    if set == 'easy':
        x = random.randint(0,10)
        m = 10
    elif set == 'medium':
        x = random.randint(0,50)
        m = 50
    elif set == 'hard':
        x = random.randint(0,100)
        m = 100
    elif set == 'expert':
        x = random.randint(0,500)
        m = 500
    elif set == 'legendary':
        x = random.randint(0, 1000000)
        m = 1000000
    elif set == 'GG':
        x = random.randint(0, 1000000000000000000)
        for _ in range(10):
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print('SECRET DIFFICULTY SELECTED')
        m = 1000000000000000000

    print('You have selected',set + '.')
    time.sleep(0.5)
    print('The number is between 0 and',str(m),'inclusive')
    time.sleep(0.5)
    print('Make your guess')

    # game #
    counter = 0
    guess = input('>> ')
    g = int(guess)
    while g != x:
        counter += 1
        if g > x:
            print('Your guess is larger than the number')
            guess = input('>> ')
            g = int(guess)
        elif g < x:
            print('Your guess is smaller than the number')
            guess = input('>> ')
            g = int(guess)
    counter += 1
    print('Congratulations! The number is',str(x))
    print('Number of guesses taken:',str(counter))


    time.sleep(1)

    replay = input('Play again? y/n : ')
    if replay == 'y':
        play = 1
    elif replay == 'n':
        play = 0

