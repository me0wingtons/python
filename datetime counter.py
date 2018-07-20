import datetime

def datetime_countdown(n):
    while n >= 0:
        i = datetime.datetime.now().second
        while datetime.datetime.now().second == i:
            continue
        print(n)
        n -= 1


import time

def time_countdown(n):
    while n:
        mins, secs = divmod(n, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        n -= 1
    print('Goodbye!')
    

for i in range(0,101):
    print(str(i)+'%', end="\r")
    time.sleep(1)
