import time
num = 0
contador = 0
while True:
    valor = int(input("Escribe un número: "))
    if valor > 10:
        while contador < 5:    
            num += 1
            time.sleep(1)
            contador += 1
            print(contador, "s")
        print("temps total: ", contador, "s")
    else:
        print("El número es menor que 10")