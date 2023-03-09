import random
import datetime

from time import sleep
def tiempo(timer):
    while timer<10:
        number = random.randint(0,10)
        if number > 0:
            sleep(1)
            timer+=1
            if timer>5:
                #time_end = datetime.datetime.now
                print("El temps ha arribat a ", timer)#-time_end)
        else:
            print("el numero és menor que 0:", timer)
            timer = 0
tiempo(0)