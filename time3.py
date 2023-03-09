import time 

start_time = 0
def tiempo():
    global start_time
    time.sleep(1)
    start_time += 1

def maquina_contador():
    num = 0
    
    while start_time < 5:
        a = float(input("Escribe un número: "))
        if a > 10:
            if num == 5:
                print("------------------------------------------------")
                print("El contador ha llegado al máximo")
                print("Has tardado ", (start_time), "segundos")
                print("------------------------------------------------")
                break
        else:
            num = 0

tiempo()
maquina_contador()