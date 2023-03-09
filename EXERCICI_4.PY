x = 0
while x <= 30:
    if x == 4 or x == 6 or x == 10:
        print("S'ha saltat el valor", x, " de x")
        x = x+1
    if x == 15:
        print("S'ha trencat l'execució del bucle quan x valia: ", x)
        break
    else:
        print("El valor del bucle es: ", x)
        x+=1