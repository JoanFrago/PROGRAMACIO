#Exercici 1 Escriu un programa que demani l’edat d’un usuari i que, en cas de ser major de 18 anys,
#aparegui el següent missatge: «Vostè és major d’edat»
edat = int(input("Quants anys tens? "))
if edat >= 18:
    print("Vostè és major d'edat")

#Exercici 2 Escriu un programa que demani dues xifres. El programa a més a més haurà de contestar
#quin dels dos és menor i quin és major, o en cas que siguin iguals, també ho indiqui.
num1 = int(input("Escriu un número "))
num2 = int(input("Ara escriu un altre "))

if num1 == num2:
    print(num1, " és igual que ", num2)
elif num1 > num2:
    print(num1, " és més gran que ", num2)
elif num1 < num2:
    print(num2, "és més gran que", num1)

#Exercici 3 Escriu un programa que demani l’any actual i la teva data de naixement, aquest programa
#ha d’indicar quina és la teva edat.
any_actual = int(input("En quin any vivim? "))
any_neixer = int(input("En quin any vas néixer? "))

print("Tens ", any_actual - any_neixer, " anys")

#Exercici 4 Escriu un programa que demani un any i escrigui si aquest és de traspàs (bisiesto)
#o no.
#Recorda que la condició per a que sigui un any de traspàs és la següent:
#« Els anys de traspàs són múltiples de 4, però els múltiples de 100 no ho són, tot i que
#els múltiples de 400 sí »
any = int(input("Escriu un any: "))
if any % 4 == 0 or any % 400 == 0:
    print("Aquest any és de traspàs.")
elif any % 100 == 0:
    print("Aquest any no és de traspàs.")
else:
    print("Aquest any no és de traspàs.")
#Exercici 5 Escriu un programa que emmagatzemi la cadena de caràcters 'contrasenya' en una
#variable, pregunti a l’usuari per la contrasenya i imprimeixi per pantalla si la contrasenya
#introduïda coincideix amb la guardada a la variable sense tenir en compte majúscules i 
#minúscules.
contrasenya = 'contrasenya'
password = str(input("Escriu la contrasenya: "))
if password.lower == contrasenya or password.upper == contrasenya:
    print("La contrasenya coincideix.")
else:
    print("La contrasenya no coincideix.")

#Exercici 6 Escriu un programa que demani al usuari un nombre enter i mostri per pantalla
#si és parell o imparell
num = int(input("Escriu un nombre enter: "))
if num % 2 == 0:
    print("El nombre ", num, " és parell.")
else:
    print("El nombre ", num, " és imparell.")

#Exercici 7 Per a poder tributar un impost, es requereix ser major de 16 anys i tenir uns
#ingressos iguals o superior a 1000€ mensuals. Escriu un programa per a que una persona
#sàpiga si ha de tributar o no
edat = int(input("Quants anys tens? "))
ingressos = float(input("Quant cobres al mes? "))

if edat >= 16 and ingressos >= 1000:
  print('Pots tributar.')
else:
  print('No pots tributar.')