import random

#############################
## INPUT YOUR ITERATION #####
#############################
iterate = int(input('set number of iterations : '))
while iterate <= 0:
    iterate = int(input('please set a number larger than 0 : '))

############ GENERATOR #####################################################

def run():
    dic = {}
    for _ in range(iterate):
        number = random.randint(0, 9999)
        if number not in dic.keys():
            dic[number] = 1
        else:
            dic[number] += 1
###########################################################################
########### ANALYSIS ######################################################
    most = list(dic.keys())[0]
    for number in list(dic.keys()):
        if dic[number] > dic[most]:
            most = number
    if iterate == 1:
        print('After running ' + str(iterate) + ' time,')
    else:
        print('After running ' + str(iterate) + ' times,')
    print('the number with most occurrence is:')
    print(str(most).zfill(4))
    print('with occurrence of ' + str(dic[most]) + ' out of ' + str(iterate))
#############################################################################

run() # comment this out if you don't want it
# ^ initial run

######## SIMULATOR #######################################################

""" lottery() checks how many tries you need before you win
the lottery. If no input is given, your chosen number is random
and it changes to another random number each time you do not win.
If an input is given, that input is your chosen number and you stay
with it until the winning number matches your chosen number.

This simulator hopes to shed some light on the controversy of the odds
of winning the lottery if you stay with a number and wait for the winning
number to match you, or you change randomly each time while the winning
number also changes randomly. """

def lottery(*n):
	l = 0
	if n:
		num = n[0]
		win = random.randint(0, 9999)
		l += 1
		while num != win:
			l += 1
			win = random.randint(0, 9999)
	else:
		num = random.randint(0, 9999)
		win = random.randint(0, 9999)
		l += 1
		while num != win:
			l += 1
			num = random.randint(0, 9999)
			win = random.randint(0, 9999)
	print('the winning number is ' + str(win).zfill(4))
	print('number of tries to win : ' + str(l))
	#return l
    
""" Feel free to create a higher order function that runs this lottery()
n number of times while keeping track of the chances of winning """


def simulate(lottery, repeats):
    win = []
    for _ in range(repeats):
        win.append(lottery)
    return sum(win)/len(win)


###########################################################################

def help():
    print('The functions available in this module are')
    print(lottery, run)
    print('you can change iterate for run()')
