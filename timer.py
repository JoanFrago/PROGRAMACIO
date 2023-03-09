import time

def timer_(num, timer):
    while num < 5:
        input_ = int(input())
        if input_ >= 10:
            while timer < 5:
                time.sleep(1)
                num += 1
                timer += 1
            if input_ < 10:
                timer = 0
                num = 0
            if timer == 5:
                print("")
                print("---------------------------------------------")
                print("El contador ha llegado a ", timer, " segundos")
                print("---------------------------------------------")
                break
timer_(0, 0)