import time

def count(t):
    while t:
        mins, secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Finished!')

tim = input('Enter your time in seconds : ')

count(int(tim))
