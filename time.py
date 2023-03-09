import datetime

def contador_(a):
    contador = 0
    while contador <= 5:
        if a > 10:
            start = datetime.datetime.now()
            contador += 1
            if contador == 5:
                print("Has trigat ", (start - end))
        else:
            stop = datetime.datetime.now()
            contador = 0
end = datetime.datetime.now()
contador_(int(input("Escriu aquí el teu valor: ")))