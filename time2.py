import time 

def maquina_contador():
    num = 0
    while num < 5:
        a = float(input("Escribe un número: "))
        if a > 10:
            start_time = time.sleep(1)
            num += 1
        else:
            num = 0
            start_time = 0
        if num == 5:
            print("------------------------------------------------")
            print("El contador ha llegado al máximo")
            print("Has tardado ", start_time, "segundos")
            print("------------------------------------------------")
            break
        
maquina_contador()